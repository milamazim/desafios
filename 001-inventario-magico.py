"""
O Desafio do Inventário Mágico 🪄

Você é um poderoso mago em um mundo de RPG tendo que gerenciar seu inventário de itens mágicos. Seu objetivo é implementar uma função que possa:

Adicionar itens ao seu inventário.
Remover itens existentes.
Listar todos os itens atuais no inventário.

Seu inventário deve ser inicializado como uma lista vazia. Os itens podem ser qualquer string que represente o nome do item, como:

📜 Pergaminho de Fogo
⚔️ Espada de Luz
🛡️ Escudo Mágico

Entrada:
Uma ação (pode ser 'adicionar', 'remover' ou 'listar') e, quando aplicável, o nome do item.

Saída:
- Para 'adicionar', retorne uma mensagem como: 'Item adicionado com sucesso.'
- Para 'remover', retorne: 'Item removido com sucesso.' ou uma mensagem de erro se o item não estiver presente.
- Para 'listar', retorne todos os itens no inventário, ou uma mensagem como: 'Inventário vazio.'

Vamos ver até onde vai sua criatividade! 💫
"""

inventario = []

def adicionar_item():
    novo_item = input('Adicionar novo item - informe o nome do item: ')
    inventario.append(novo_item)
    print("Item adicionado com sucesso.")
    

def remover_item():
    listar_itens()
    
    if inventario:
        remover_item = int(input('Remover item - informe o índice: '))

        try:
            inventario.pop(remover_item)
            print("Item removido com sucesso.")
        except IndexError:
            print('Item não existe')
    

def listar_itens():
    if inventario:
        for i in range(len(inventario)):
            print(f'Item [{i}]: {inventario[i]}\n')        
    else:
        print('Inventário está vazio.')

def texto_menu():
    print(
    '-------------------------------------------------\n' +
    '               INVENTARIO MAGICO  \n' +
    '-------------------------------------------------\n' +
    '1 - Adicionar itens \n' +
    '2 - Remover itens \n' +
    '3 - Listar itens \n' +
    '4 - Encerrar\n'
    '-------------------------------------------------')

def menu():
    opcao = input('(menu principal) Digite a opção desejada: ')
        
    match opcao:
        case "1":
            adicionar_item()
            menu()            
        case "2":
            remover_item()
            menu()
        case "3":
            listar_itens()
            menu()
        case "4":
            print("Programa encerrado com sucesso.")
        case _:  # 'default' case
            print("Valor digitado não corresponde a nenhuma opção.")
            menu()

texto_menu()
menu()