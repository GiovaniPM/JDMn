import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("date.json")

dados = {}
dados['data'] = '01/06/2024'

desconto, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('Resultado é:', desconto)