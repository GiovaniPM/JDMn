import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("desconto.json")

dados = {}
dados['Preco'] = 501
dados['Categoria'] = 'vestuario'

desconto, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('Desconto é de:', desconto)