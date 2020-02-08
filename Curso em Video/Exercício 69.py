p = 0
h = 0
m20 = 0
while True:
    print("===" * 20)
    n1 = int(input("\033[0;31mDigite a sua idade: "))
    n2 = str(input("Qual é o seu sexo? [M/F] ")).upper()
    n3 = str(input("Quer continuar? [S/N] \033[m")).upper()
    if n1 > 18:
        p += 1
    if n2 == "M":
        h += 1
    if n1 < 20 and n2 == "F":
        m20 += 1
    if n3 == "N":
        break
print(f"Há {p} pessoa(s) com mais de 18 anos.")
print(f"Foram cadastrados {h}, homens.")
print(f"Há {m20} mulher com menos de 20 anos.")
