soma = 0
homem = 0
n1 = 0
mulher = 0
for dados in range(1, 5):
    nome = str(input(f"Digite o {dados}º nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo. M para Masculino e F para Feminino: ")).upper()
    soma += idade
    media = soma/4
    if dados == 1 and sexo == "M":
        homem = idade
        n1 = nome
    else:
        if idade > homem:
            homem = idade
            n1 = nome
    if sexo == "F" and idade < 20:
        mulher += 1
print("\033[1;31m=="*25)
print(17*" ", "ANALISANDO DADOS!")
print("=="*25, "\033[m")
print(f"A média de idade do grupo é {media}")
print(f"O nome homem mais velho é {n1}")
print(f"Existe {mulher} mulheres com menos de 20 anos.")
