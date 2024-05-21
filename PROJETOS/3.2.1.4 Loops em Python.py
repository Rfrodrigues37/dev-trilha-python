import time

# = Contando de 1 a 100 com while
#i = 0       
#while i < 100:
#    print(i + 1) 
#    i += 1


# - Contando de 1 a 100 com for
#for i in range(10, 50, 2): #A função range() também pode aceitar três argumentos - dê uma vista de olhos ao código no editor.
#    pass
#    print(i)


# - Elevar um numero a uma potencia, expo conta de um a 16, power é o multiplicador
#power = 1
#for expo in range(16): 
#    print("2 Elevado a", expo, "is", power)  
#    power *= 2 # Multiplica o valor da variável pelo valor do operando à direita e, em seguida, atribui o resultado de volta à variável.



#    time.sleep(1)

#BREAK
#pal_sec = "chupacabra"
#a = True

#while True:
#    palavra = str(input("Digite uma palavra: "))
#    if palavra == pal_sec:
#        print("You've successfully left the loopVocê saiu do loop com sucesso.")
#        break
#    else:
#        
#        a = False


#user_word = input("insira uma palavra: ")
#for letter in user_word:
#    # Verifica se a letra é uma vogal
#    if letter in ['A', 'E', 'I', 'O', 'U']:
#        # Se for uma vogal, usa 'continue' para pular o resto do loop
#        continue
#    print(letter, end="")   

import math

while True:
    blocos = int(input("Digite o número de blocos (ou digite 0 para sair): "))
    
    if blocos == 0:
        print("Programa encerrado.")
        break
    
    def calcular_altura(num_blocos):
        altura = math.sqrt(2 * num_blocos + 1/4) - 1/2
        return altura
    
    altura_piramide = calcular_altura(blocos)
    
    altura_piramide_arredondada = math.floor(altura_piramide)  # Arredondando a altura para baixo
    
    print(f"A altura da pirâmide com {blocos} blocos é {altura_piramide_arredondada} unidades.")

