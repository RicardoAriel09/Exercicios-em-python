r = int(input("Digite um número: "))
total = 0
for n in range(1, r + 1):
    if r % n == 0:
        print("\033[31m", end=" ")
        total = total + 1
    else:
        print("\033[33m", end=" ")
    print(f"{n}", end=" ")
# print(f"\nO número total de divisores é {total} ")

if total > 2:
    print(f"\nO número total de divisores é {total}. Logo este número não é primo!")
else:
    print(f"\nEste número só tem {total} divisores. Então ele é um número primo!")
