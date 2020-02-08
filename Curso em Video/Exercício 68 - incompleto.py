from random import random
c = random("P", "I")
print("==="*20)
print(" " * 18, "Jogo do Par ou Impar!")
print("==="*20)
print(c)
while True:
    n1 = str(input("Você quer para ou Impar? [P/I] "))

    if n1 == c:
        print(c)
