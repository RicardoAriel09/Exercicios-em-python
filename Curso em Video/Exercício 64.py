n1 = 0
c = 0
while n1 == 0:
    n2 = int(input("Digite um número: "))
    c += n2
    if n2 == 999:
        n1 = 1
print(f"A soma dos valores digitados é {c - 999}.")
