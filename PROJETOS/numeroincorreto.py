import time
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
flag = True
while flag:
    try:


        n = int(input("Digite qual numero você imagina = "))
        if n == 777:
            print("Parabens você acertou")
            time.sleep(1)
            flag = False
        else:
            print("Numero incorreto, tente novamente")
            time.sleep(1)

    except ValueError:

            print("Isto não eh um numero Bah")
            time.sleep(1)