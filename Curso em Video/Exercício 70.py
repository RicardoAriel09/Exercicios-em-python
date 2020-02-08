print("\033[0;34m===" * 20)
print(" " * 20, "LOJÃO SUPER TOP")
print("===" * 20, "\033[m")
c = 0
m = 0
while True:
    n1 = str(input("Digite o nome do produto: ")).upper()
    n2 = int(input("Digite o preço do produto. R$: "))
    n3 = str(input("Quer continuar? [S/N] ")).upper()
    c += n2
    d = 0
    a = n1
    if n2 >= 1000:
        m += 1
    if n2 > d:
        d = n2
        a = n1
    if n3 == "N":
        break
print("\033[0;32m===" * 20)
print(" " * 23,"Informações")
print("===" * 20, "\033[m")
print(f"\033[0;33m1 - O total gasto na compra foi de R$ {c}.")
print(f"2 - Total de produtos acima de R$ 1000 é {m}")
print(f"3 - O produto mais barato é {a} e custa R$ {d}.\033[m")