c = 0
n = 0
while True:
    n1 = int(input("Digite um número, 'Digite 999 para sair': "))
    if n1 == 999:
        break
    c += n1
    n += 1
print(f"Foi digitado {n} número(s) e a soma total foi {c}.")
