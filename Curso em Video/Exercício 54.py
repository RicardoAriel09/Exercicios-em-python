from time import strftime
n1 = int(strftime("%Y"))
c1 = 0
c2 = 0
for r in range(1, 8):
    n2 = int(input(f"{r}º Digite o ano em que você nasceu: "))
    t = n1 - n2
    if t >= 18:
        c1 += 1
    else:
        c2 += 1
print(f"\033[31mHá {c1} pessoas que tem mais de 18 anos.")
print(f"Há {c2} pessoas que tem menos de 18 anos.\033[m")

# from time import datetime
# n1 = datetime.today().year
# Outra opção para mostrar o ano!
# Clean code = dá para diminuir o tamanho do código!
