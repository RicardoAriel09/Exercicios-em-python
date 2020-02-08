from random import randint
cont = 0
acertou = False
while not acertou:
    n1 = randint(0, 10)
    n2 = int(input("Digite um número de 0 à 10: "))
    if n2 == n1:
        cont += 1
        print(f"Você ganhou, na {cont}ª tentativa! parabéns!!!")
        acertou = True
    else:
        print("Tente novamente!")
        print(n1)
        cont += 1
# poderia ser feito usando o break, deixado while True: