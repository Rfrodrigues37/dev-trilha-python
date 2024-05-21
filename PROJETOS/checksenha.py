import time

repetir = True

while repetir:
    try:
        a = int(input("Digite um numero = "))
        if a == 2277:
            print("Senha correta..")
            time.sleep(0.5)
            print("Fechando programa..")
            time.sleep(1)
            repetir = False
        else:
            print("Senha incorreta...")
            time.sleep(0.5)
            print("Tente novamente...")
            time.sleep(1)
    except ValueError:
            print("O valor não corresponde a um numero")
            time.sleep(0.5)
            print("Tente novamente...")
            time.sleep(1)
