import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("set.json")

dados = {}
dados['colunaUm'] = "4"

desconto, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('Retorno é:', desconto)