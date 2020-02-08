# for r in range(1, 501):
#    if r % 2 == 1 and r % 3 == 0:
#        print(r, end=" -> ")

soma = 0
c = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        # print(a, end=" ")
        soma = soma + a
        c = c + 1
print(f"Os impares múltiplos de três de 1 até 500, são {c} e a soma deles dá {soma}")
