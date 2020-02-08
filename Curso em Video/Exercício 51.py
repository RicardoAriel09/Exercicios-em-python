n1 = int(input('\033[0;33mDigite o primeiro termo da P.A: '))
n2 = int(input('Digite a razão da P.A: \033[m'))
print("\n")
for n in range(1, 13):
    for p in range(0, 1):
        pa = n1 + (n - 1) * n2
        print("\033[0;31mO {}º termo da P.A é {}\033[m.".format(n, pa))
