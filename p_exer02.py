lista = []
num = int(input('Digite um número: '))
for i in range(num):
    while True:
        valor = int(input(f'Digite o {i+1}º valor: '))
        if valor not in lista:
            lista.append(valor)
            break
        else:
            print(f'valor {valor} já existe, digite novamente')

lista.sort()
print(lista)