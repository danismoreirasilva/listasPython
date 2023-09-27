lista = []
maior = menor = 0

for i in range(5):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))

for i, valor in enumerate(lista):
    if i == 0:
        maior = menor = valor
    else:
        if valor >= maior:
            maior = valor
        if valor <= menor:
            menor = valor

print(lista)

indiceMenor = []
indiceMaior = []
for i, valor in enumerate(lista):
    if valor == menor:
        indiceMenor.append(i)

for i, valor in enumerate(lista):
    if valor == maior:
        indiceMaior.append(i)
print(f'\nO menor valor é o {menor} nas posições: {indiceMenor}')
print(f'O maior valor é o {maior} nas posições: {indiceMaior}')
