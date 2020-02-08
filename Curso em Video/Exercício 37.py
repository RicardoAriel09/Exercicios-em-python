n1 = int(input("Digite um número inteiro: "))
print(
"""Digite [1] para converter em Binário.
Digite [2] para converter em Octal.
Digite [3] para converter em Hexadecimal.""")
n2 = int(input("Digite sua escolha: "))

if n2 == 1:
    print("Em binário o número {}, fica {}".format(n1,bin(n1)[2:]))
elif n2 == 2:
    print("Em Octal o número {}, fica {}.".format(n1,oct(n1)[2:]))
elif n2 == 3:
    print("Em Hexadecimal o número {}, fica {}.".format(n1,hex(n1)[2:]))
else:
    print("Você digitou {}, volte e escolha uma das opções!".format(n2))