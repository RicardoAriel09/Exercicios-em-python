maior = 0
menor = 0
for peso in range(1, 6):
    n1 = float(input(f"Digite o {peso}º peso: "))
    if peso == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print(f"O maior peso lido foi de {maior} Kg.")
print(f"O menor peso lido foi de {menor} Kg.")