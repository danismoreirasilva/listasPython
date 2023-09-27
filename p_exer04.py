lista = []
for i in range(5):
    num = int(input(f'Digite o {i+1}° valor: '))
    #lista[-1] é o ultim elemento da lista, ou, lista[len(lista)-1]
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for j in range(len(lista)):
            if num < lista[j]:
                lista.insert(j, num)
                break

print(lista)


