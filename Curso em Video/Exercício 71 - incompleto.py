print("=" * 30)
print("{:^30}".format("BANCO RARIEL Inc"))
print("=" * 30)
valor = int(input("Quanto em R$ você deseja sacar: "))
total = valor
notas = 50
t = 0
while True:
    if total >= 50:
        total -= 50
        t += 1
#        if total == 20:



    else:
        break
print(total)
print(t)