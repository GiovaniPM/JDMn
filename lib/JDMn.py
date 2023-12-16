from datetime import date, datetime

import json
import re

date_format  = "%d/%m/%Y" # DD/MM/YYYY
dmnOperators = [ '== ', '<= ', '>= ', '< ', '> ', 'not in ', 'in ' ]
valid_types  = ['string', 'number', 'date', 'boolean']

def splitRule(rule):
    """_summary_

    Args:
        rule (_type_): _description_

    Returns:
        _type_: _description_
    """
    pos = 0
    sel = -1
    for operator in dmnOperators:
        count = rule.count(operator)
        if count > 0 and sel < 0:
            sel = pos
        pos += 1
    if sel > -1:
        oper = dmnOperators[sel]
        rule = rule.replace(oper, '')
    else:
        oper = ""
        rule = ""
    return oper, rule

def existOperator(value):
    """Verify into expression rule if exists a valid operator

    Args:
        value (string): expression rule

    Returns:
        boolean: true if the expression rule exists inside a valid operator
    """
    for operator in dmnOperators:
        count = value.count(operator)
        if count > 0:
            return True
    return False

def strToDate(value):
    """Convert a string date such DD/MM/YYYY in a Python date object

    Args:
        value (string): a string with date format DD/MM/YYYY

    Returns:
        string: string with date object Python such date(YYYY, MM, DD)
    """
    date_object  = datetime.strptime(value, date_format)
    day = date_object.day
    month = date_object.month
    year = date_object.year
    return "date(" + str(year) + ", " + str(month) + ", " + str(day) + ")"

def getDefinitionsJDMn(fileName):
    """Open a JDMn file (*.json) and get de decisionTable

    Args:
        fileName (string): The filename

    Returns:
        Dict: The decision table
    """
    with open(fileName, "r") as arquivo:
        dados = json.load(arquivo)
    
    definitions   = dados         ['definitions'   ]
    decision      = definitions   ['decision'      ]
    decisionTable = decision      ['decisionTable' ]
    
    return decisionTable

def castingValues(typeToCast, value):
    """Turn the value as the typeDef definition

    Args:
        typeToCast (string): The typeDef definition
        value (class): type cast of the original value

    Returns:
        string: the representation of the value to be useb in the evaluate function
    """
    if value is not None:
        if typeToCast == 'number':
            if str(type(value)) != "<class 'float'>":
                value = float(value)
        elif typeToCast == 'string':
            if str(type(value)) != "<class 'str'>":
                value = str(value)
        elif typeToCast == 'date':
            if str(type(value)) != "<class 'str'>":
                value = str(value)
            value = strToDate(value)
    
    return value

def evaluateJDMn(decisionTable, dictToEvaluate, debbugJDMn = None):
    """_summary_

    Args:
        decisionTable (_type_): _description_
        dictToEvaluate (_type_): _description_
        debbugJDMn (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    inputs  = decisionTable ['input'  ]
    rules   = decisionTable ['rule'   ]
    
    values      = []
    types       = []
    expressions = []
    results     = []
    tests       = []
    
    if debbugJDMn != None:
        print(inputs)
        print('----')
        print(dictToEvaluate)
        print('----')
        print(rules)
        print('----')
    
    for input in inputs:
        expression = input         ['inputExpression']
        label      = expression    ['label'          ]
        value      = dictToEvaluate[label            ]
        typeValue  = expression    ['typeRef'        ]
        
        types.append(typeValue)
        values.append(castingValues(typeValue, value))
    
    for rule in rules:
        entrys = rule['inputEntry']
        output = rule['outputEntry']
        
        expression = []
        pos        = 0
        
        # Build the expressions to evaluate
        for entry in entrys:
            if values[pos] == '' or values[pos] == None:
                if entry['text'] == '' or entry['text'] == None:
                    expression.append('True')
                else:
                    expression.append('False')
            elif entry['text'] == '' or entry['text'] == None:
                expression.append('True')
            elif types[pos] == 'number':
                if existOperator(entry['text']):
                    expression.append(str(values[pos]) + " " + entry['text'])
                else:
                    expression.append(str(values[pos]) + " == " + entry['text'])
            elif types[pos] == 'boolean':
                if existOperator(entry['text']):
                    expression.append(str(values[pos]) + " " + entry['text'])
                else:
                    expression.append(str(values[pos]) + " == " + entry['text'])
            elif types[pos] == 'date':
                s = entry['text']
                match = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', s)
                if match:
                    date_string = match.group(1)
                    value = strToDate(date_string)
                    s = s.replace(date_string, value)
                if existOperator(entry['text']):
                    expression.append(str(values[pos]) + " " + s)
                else:
                    expression.append(str(values[pos]) + " == " + s)                    
            elif types[pos] == 'string':
                if existOperator(entry['text']):
                    expression.append("'" + values[pos] + "' " + entry['text'])
                else:
                    expression.append("'" + values[pos] + "' == " + entry['text'])
            
            pos += 1
        
        results.append(output['text'])
        expressions.append(expression)
    
    pos = 0
    generalError = False
    
    for line in expressions:
        test = True
        exceptValue = False
        for column in line:
            if test == True:
                try:
                    test = eval(column)
                except:
                    print('\033[91m', line, '--> (', results[pos], ') ** Error **\033[0m')
                    exceptValue = True
                    generalError = True
                    test = False
        tests.append(test)
        if debbugJDMn != None:
            if exceptValue != True:
                if test:
                    print('\033[32m', line, '--> (', results[pos], ')', test, '\033[0m')
                else:
                    print('\033[34m', line, '--> (', results[pos], ')', test, '\033[0m')
        pos += 1
    
    pos       = 0
    outputPos = -1
    
    for test in tests:
        if test == True and outputPos == -1:
            outputPos = pos
        pos += 1
    
    if outputPos > -1 and generalError != True:
        valueReturned = results[outputPos]
    else:
        valueReturned = None
    
    if str(type(valueReturned)) != "<class 'str'>":
        valueReturned = valueReturned
    else:
        valueReturned = valueReturned.replace("'", "")
    
    return valueReturned, expressions[outputPos]