"""
n1 = int(input("Digite o primeiro termo da P.A: "))
n2 = int(input("Digite a Razão da P.A: "))
c = 0
print("=-=" * 30)
while c < 10:
    c += 1
    pa = n1 + (c - 1) * n2
    print(f"{c}º termo é {pa}")
print("=-=" * 30)
n3 = str(input("Quer mostrar mais 5 termos? [S/N] ")).upper()
while True:
    if n3 == "S":
        c += 1
        pa = n1 + (c - 1) * n2
        print(f"{c}º termo é {pa}")
        break
    else:
        print("Fim do Programa!") """

print("Gerador de PA v3.0")
print("=-=" * 15)
n1 = int(input("Primeiro termo: "))
n2 = int(input("Razão da PA: "))
t = n1
c = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while c <= tot:
        print(f"{t} → ", end="")
        t += n2
        c += 1
    print("Pausa.")
    m = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {tot} termos mostrados.")
