import json

def getDefinitionsJDMn(fileName):
    with open(fileName, "r") as arquivo:
        dados = json.load(arquivo)
    
    definitions   = dados         ['definitions'   ]
    decision      = definitions   ['decision'      ]
    decisionTable = decision      ['decisionTable' ]
    
    return decisionTable

def castingValues(typeToCast, value):
    if value is not None:
        if typeToCast == 'number':
            if type(value) != "<class 'float'>":
                value = float(value)
        elif typeToCast == 'string':
            if type(value) != "<class 'str'>":
                value = str(value)
    
    return value

def evaluateJDMn(decisionTable, dictToEvaluate, debbugJDMn = None):
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
            if entry['text'] == '' or entry['text'] == None:
                expression.append('True')
            elif values[pos] == None or values[pos] == '':
                expression.append('True')
            elif types[pos] == 'number':
                expression.append(str(values[pos]) + " " + entry['text'])
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