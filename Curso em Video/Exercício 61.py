"""
n1 = int(input("Digite o primeiro termo da P.A: "))
n2 = int(input("Digite a Razão da P.A: "))
c = 0

while c < 10:
    c += 1
    pa = n1 + (c - 1) * n2
    print(f"{c}º termo é {pa}") """

print("Gerador de PA v2.0")
print("=-=" * 15)
n1 = int(input("Primeiro termo: "))
n2 = int(input("Razão da PA: "))
t = n1
c = 1
while c <= 10:
    print(f"{t} → ", end="")
    t += n2
    c += 1
print("Fim")
