t = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete","oito", "nove", "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezeseis", "dezessete", "dezoito", "dezenove", "vinte" )
num = int(input("Digite um número inteiro: "))
for cont in range(0, len(t)):
    if num == cont:
        print(f"O número digitado foi {t[cont]}.")