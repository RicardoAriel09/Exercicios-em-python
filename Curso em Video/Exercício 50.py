soma = 0
for r in range(1, 7):
    f = int(input(f"Digite o {r}º número: "))
    if f % 2 == 0:
        soma = soma + f
print(f"A soma dos números pares digitados é {soma}.")
