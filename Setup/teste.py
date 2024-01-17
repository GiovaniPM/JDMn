import os

def modificar_caminho_e_extensao(filepath, nova_extensao, novo_diretorio, posicao):
    # Verifica se a nova extensão começa com um ponto
    if not nova_extensao.startswith('.'):
        nova_extensao = '.' + nova_extensao
    
    # Divide o caminho do arquivo em partes
    partes = filepath.split(os.sep)
    
    print(partes)
    
    # Insere o novo diretório na posição desejada
    partes.insert(posicao, novo_diretorio)

    print(partes)

    
    # Junta as partes novamente, formando o novo caminho
    novo_caminho = os.sep.join(partes)
    
    # Separa o nome do arquivo da extensão atual
    base, _ = os.path.splitext(novo_caminho)
    
    # Retorna o novo caminho do arquivo com a nova extensão
    return base + nova_extensao

# Exemplo de uso da função
caminho_original = '\\caminho\\para\\o\\arquivo.txt'
nova_extensao = 'md'
novo_diretorio = 'subdiretorio'
posicao = 4  # A posição onde o novo diretório deve ser inserido

caminho_modificado = modificar_caminho_e_extensao(caminho_original, nova_extensao, novo_diretorio, posicao)
print(caminho_modificado)  # Saída: '/caminho/para/subdiretorio/o/arquivo.md'
