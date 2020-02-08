m = 1
s = 0
n1 = 0
while n1 == 0:
    if n3 == "S":
        n2 = int(input("Digite um número: "))
        s += n2
        m += 1
        n3 = str(input("Quer continuar digitando? [S/N] ")).upper()
    else:
        n1 = "N"
print(f"A média dos valores digitados é {s/m}")

