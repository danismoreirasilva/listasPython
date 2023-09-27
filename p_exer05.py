'''Crie um programa que vai ler vários números e inserir em uma lista,
conforme o usuário desejar continuar. Depois disso:
a)	Quantos números foram digitados
b)	A lista de valores ordenada de forma decrescente
c)	Se o valor 5 foi digitado e está ou não na lista'''

listaNum = []
while True:
    while True:
        try:
            listaNum.append(int(input('Digite um número: ')))
            break
        except:
            print(f'Erro: Você deve digitar um valor numérico!')

    while True:
        continuar = str(input('Deseja continuar (s)im ou n(ão): ')).lower().strip()
        if continuar in 'sn':
            break
        else:
            print('Erro. Você só pode digitar "s" ou "n"!')

    if continuar == 'n':
        listaNum.sort(reverse=True)
        break

print(f'Foram digitados {len(listaNum)} números.')
print(f'A lista em ordem decrescente é {listaNum} ')
if 5 in listaNum:
    print(f'O valor 5 está na lista.')
else:
    print(f'O valor 5 não está na lista.')
print(f'Você saiu do programa!')
