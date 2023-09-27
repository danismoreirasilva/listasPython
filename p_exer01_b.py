lista = []
for i in range(5):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))

indiceMenor = []
indiceMaior = []
indices = []
for i, valor in enumerate(lista):
    if valor == max(lista) and valor == min(lista):
        indices.append(i+1)
    elif valor == max(lista):
        indiceMaior.append(i+1)
    elif valor == min(lista):
        indiceMenor.append(i+1)

print(f'A lista é: {lista}')
if len(indices) > 0:
    print(f'O único valor digitado foi: {max(lista)}, nas posições: {indices}')
else:
    print(f'Maior elemento da lista é: {max(lista)}, nas posições: {indiceMaior}')
    print(f'Menor elemento da lista é: {min(lista)}, nas posições: {indiceMenor}')