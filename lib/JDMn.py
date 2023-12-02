from datetime import date, datetime

import json
import re

def getDefinitionsJDMn(fileName):
    """_summary_

    Args:
        fileName (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(fileName, "r") as arquivo:
        dados = json.load(arquivo)
    
    definitions   = dados         ['definitions'   ]
    decision      = definitions   ['decision'      ]
    decisionTable = decision      ['decisionTable' ]
    
    return decisionTable

def castingValues(typeToCast, value):
    """_summary_

    Args:
        typeToCast (_type_): _description_
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    date_format = "%d/%m/%Y"
    
    if value is not None:
        if typeToCast == 'number':
            if type(value) != "<class 'float'>":
                value = float(value)
        elif typeToCast == 'string':
            if type(value) != "<class 'str'>":
                value = str(value)
        elif typeToCast == 'date':
            if type(value) != "<class 'str'>":
                value = str(value)
            date_object  = datetime.strptime(value, date_format)
            day = date_object.day
            month = date_object.month
            year = date_object.year
            value = "date(" + str(year) + ", " + str(month) + ", " + str(day) + ")"
    
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
    date_format = "%d/%m/%Y"
    
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
        
        for entry in entrys:
            if values[pos] == '' or values[pos] == None:
                if entry['text'] == '' or entry['text'] == None:
                    expression.append('True')
                else:
                    expression.append('False')
            elif entry['text'] == '' or entry['text'] == None:
                expression.append('True')
            elif types[pos] == 'number':
                expression.append(str(values[pos]) + " " + entry['text'])
            elif types[pos] == 'date':
                s = entry['text']
                match = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', s)
                if match:
                    date_string = match.group(1)
                    date_object = datetime.strptime(date_string, date_format)
                    day = date_object.day
                    month = date_object.month
                    year = date_object.year
                    value = "date(" + str(year) + ", " + str(month) + ", " + str(day) + ")"
                    s = s.replace(date_string, value)
                expression.append(str(values[pos]) + " " + s)
            elif types[pos] == 'string':
                expression.append("'" + values[pos] + "' == '" + entry['text'] + "'")
            
            pos += 1
        
        results.append(output['text'])
        expressions.append(expression)
    
    pos = 0
    
    for line in expressions:
        test = True
        for column in line:
            if test == True:
                test = eval(column)
        tests.append(test)
        if debbugJDMn != None:
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
    
    return results[outputPos], expressions[outputPos]