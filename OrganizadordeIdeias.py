import json
import time
dicionario = dict()
lista = list()

opcao = int(input('''Bem vindo(a) ao Organizador de Ideias!\n
Selecione uma opção para continuar:
[1] Ver todos os tópicos e ideias
[2] Adicionar ideia
\nDigite sua resposta: '''))

if opcao == 1:

    print("\nMostrando listagem...\n")
    time.sleep(1)

    with open('lista.json', 'r', encoding='UTF-8') as a:
        dicionario = json.load(a)
    
    # Pega tópicos do dicionário e coloca-los em uma lista
    chaves = list(dicionario.keys())

    # Repetição para mostrar todos os tópicos do dicionário
    for a in range(0, len(dicionario.keys())):
        topico = chaves[a]
        chaves[a] = dicionario[topico]
        time.sleep(1)
        print(f"----- {topico} -----")
        time.sleep(0.5)

        # Verifica os elementos (ideias) que estão em uma lista para uma melhor formatação
        for i in range(0,len(chaves[a])):
            if type(chaves[a][i]) == list:
                print("=> ",chaves[a][i][0])
                time.sleep(0.5)
            else:
                print("=> ",chaves[a][i])
                time.sleep(0.5)
        print(end='\n')
        


if opcao == 2:

    topico = str(input('Digite o tópico da ideia: ')).capitalize()
    ideia = str(input(f'Digite a ideia para {topico}: ')).strip().capitalize()
    lista.append(ideia)

    with open('lista.json', 'r', encoding='UTF-8') as a:
        dicionario = json.load(a)

    if topico in dicionario and isinstance(dicionario[topico], list):
        dicionario[topico].append(lista)
        print('Ideia adicionada com sucesso!\n')
        time.sleep(1)
        print("Resultado:\n")
        time.sleep(1)
        print(f"----- {topico} -----")
        for i in range(0,len(dicionario[topico])):
            if type(dicionario[topico][i]) == list:
                print("=> ", dicionario[topico][i][0])
                time.sleep(0.5)
            else:
                print("=> ",dicionario[topico][i])
                time.sleep(0.5)
        print(end='\n')

    else:
        dicionario[topico] = lista
        print(f'Novo tópico {topico} criado.\n')
        time.sleep(1)
        print(f"----- {topico} -----")
        print(f"=> {dicionario[topico][0]}\n")

    with open('lista.json', 'w', encoding='UTF-8') as a:
        json.dump(dicionario, a, indent=2, ensure_ascii=False)


