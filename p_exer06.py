'''Crie um programa que vai ler vários números e inserir em uma lista,
conforme o usuário desejar continuar. Depois disso:
crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das 3 listas geradas.'''

listaNum = []
listaPares = []
listaImpares = []

while True:
    while True:
        try:
            listaNum.append(int(input('Digite um número: ')))
            break
        except:
            print(f'Erro: Você deve digitar um valor numérico!')

    continuar = str(input('Deseja continuar (s)im ou n(ão): ')).lower().strip()
    if continuar == 'n':
        break

for i, v in enumerate(listaNum):
    if v % 2 == 0:
        listaPares.append(v)
    else:
        listaImpares.append(v)

print(f'A lista de entrada é: {listaNum}')
if len(listaPares) > 0:
    print(f'A lista de pares é: {listaPares}')
else:
    print(f'Não foram digitados valores pares.')
if len(listaImpares) > 0:
    print(f'A lista de ímpares é: {listaImpares}')
else:
    print(f'Não foram digitados valores ímpares.')
