
s = 0
while s != "M" or "F":
    s = str(input("Digite M para masculino e F para feminino: ")).upper()
    if s == "M":
        print("Você digitou {}. Seu sexo é masculino! ".format(s))
    elif s == "F":
        print("Você digitou {}. Seu sexo é feminino!".format(s))
    else:
        print("Você digitou errado tente novamente!")