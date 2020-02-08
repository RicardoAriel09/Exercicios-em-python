print("\033[1;31mNúmeros pares entre 1 e 50\033[m")
for r in range(1, 51):
    if r % 2 == 0:
        print(r, end=" -> ")
