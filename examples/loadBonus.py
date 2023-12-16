import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("bonus.json")

dados = {}
dados['cargo'] = "gerente"
dados['desempenho'] = "bom"

desconto, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('Bonus é de:', desconto)