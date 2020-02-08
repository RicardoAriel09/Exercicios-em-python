from random import randint
num = int(input("Digite um número de 0 a 5: "))
n1 = randint(0, 5)
if num == n1:
    print("Você ganhou. Parabéns!!!")
else:
    print("Você perdeu!!!")