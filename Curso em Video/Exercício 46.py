from time import sleep
print("\033[1;31m=="*50)
print(35*" ","Contagem Regressiva!")
print("=="*50, "\033[m")
for r in range(10, 0, -1):
    sleep(1)
    print(r)
print("Acabou!")
