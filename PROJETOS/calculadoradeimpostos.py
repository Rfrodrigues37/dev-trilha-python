flag = True

while flag: #trava o programa em loop

    rendimento = float(input("Digite seu rendimento em thalers = "))
    if rendimento < 85528:
        taxa = ((rendimento * 18)/100 - 556.2) # o imposto era igual a 18% do rendimento menos 556 thalers e 2 cêntimos
        print("Valor abaixo do limite o IRS é de = ", taxa)
    
    
    else:
        taxa = (14839.2 + (((rendimento - 85528) * 32) /100)) #o imposto seria igual a 14.839 thalers e 2 cêntimos, mais 32% do excedente 
        print("Valor excedeu o limite do o IRS é de = ", taxa)