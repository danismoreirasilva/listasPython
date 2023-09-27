lista = []
i = 1
while True:
    while True:
        valor = int(input(f'Digite o {i}º valor: '))
        if valor not in lista:
            lista.append(valor)
            i += 1
            break
        else:
            print(f'valor {valor} já existe, digite novamente')

    while True:
        continuar = str(input('Deseja continuar do programa (S)im ou (Não): ')).lower()
        if continuar not in 'sn':
            print(f'Erro: Você só pode digitar s ou n!')
        else:
            break

    if continuar == 'n':
        break

lista.sort()
print(f'A lista é: {lista}!')
print('O programa foi encerrado!')