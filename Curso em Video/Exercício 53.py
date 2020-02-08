frase = str(input("Digite uma frase: ")).upper().strip()
divisao = frase.split()
soma = "".join(divisao)
inverso = ""
for letra in range(len(soma) - 1, -1, -1):
    inverso += soma[letra]
if soma == inverso:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")

# inverso = soma[::-1]
# Outra solução usando fatiamento para resolver o exercício.
