import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("Dish.json")

dados = {}
dados['season'] = "'Spring'"
dados['guestCount'] = 2

dish, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

JDMnDefs = JDMn.getDefinitionsJDMn("Beverages.json")

dados = {}
dados['dish'] = "'" + dish + "'"
dados['children'] = False

beverage, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('The dish is: ' + dish + ' and beverage: ' + beverage)