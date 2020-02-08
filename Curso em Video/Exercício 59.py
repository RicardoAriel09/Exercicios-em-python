from time import sleep
n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
acabou = False
while not acabou:
    print('''    [ 1 ] Somar.
    [ 2 ] Multiplicar.
    [ 3 ] Maior.
    [ 4 ] Novos Número.
    [ 5 ] Sair do Programa.''')
    n3 = int(input(">>>>> Qual é a sua opção? "))
    if n3 == 1:
        print(f"A soma de {n1} + {n2} é igual à {n1 + n2}.")
        print("=-=" * 15)
    if n3 == 2:
        print(f"A multiplicação de {n1} x {n2} é igual à {n1 * n2}.")
        print("=-=" * 15)
    if n3 == 3:
        if n1 > n2:
            print(f"O Número {n1} é maior que {n2}.")
            print("=-=" * 15)
        elif n1 < n2:
            print(f"O número {n2} é maior que {n1}.")
            print("=-=" * 15)
        else:
            print("Os números digitados são iguais.")
            print("=-=" * 15)
    if n3 == 4:
        print("Informe novos números.")
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo Valor: "))
        print("=-=" * 15)
    if n3 == 5:
        print("Finalizando...")
        sleep(2)
        print("=-=" * 15)
        print("Fim do Programa! Volte Sempre!")
        acabou = True
    if n3 > 5 or n3 < 1:
        print("Opção inválida. Tente Novamente!")
        print("=-=" * 15)
