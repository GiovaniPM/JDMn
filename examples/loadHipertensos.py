import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("hipertensos.json")

dados = {}
dados['PAS'] = None
dados['PAD'] = 60
dados['Riscos'] = 3
dados['CondClinicas'] = "N"

desconto, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('Risco é :', desconto)