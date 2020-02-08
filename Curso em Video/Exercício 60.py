"""
n1 = int(input("Digite um número para saber seu fatorial: "))
f = 1
for c in range(1, n1):
    f = f * c
print(f"O fatorial de {n1}! é {f*n1}") """

# from math import factorial
# n1 = int(input('Digite um número: '))
# f = factorial(n1)
# print(f"O fatorial de {n1} é {f}.")

n1 = int(input("Digite um número para saber seu fatorial: "))
c = n1
f = 1
print(f"Calculando {n1}! = ", end='')
while c > 0:
    print(f"{c}", end='')
    print(" x " if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f, end='')