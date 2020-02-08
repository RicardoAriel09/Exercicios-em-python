print(" " * 15, "Tabuada")
print("--"*20)
while True:
    n1 = int(input('Digite um número: '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f"{n1} X {c} = {n1 * c}")
print("FIM DO PROGRAMA !!!")
