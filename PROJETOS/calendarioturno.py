import datetime

#Função que captura o dia, mês e ano digitados
#Confere se o dado digitado é correto, e traz um erro caso nao sejam
data_start = datetime

#validador de data formato xx/xx/xxxx
def validar_data(data_str):
    try:
        data = datetime.datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        return None
#captura dada do teclado    
def capturar_data():
    while True:
        try:
            data_str = input("Digite a data (dd/mm/aaaa): ")
            data = validar_data(data_str)
            if data:
                return data
            else:
                print("Data inválida. Por favor, insira uma data válida no formato dd/mm/aaaa.")
        except ValueError:
            print("Formato inválido. Por favor, insira a data no formato dd/mm/aaaa.")


#compara quantos dias se passaram entre as
def dias():
    data_inicio = datetime(2024, 1, 3)
    data_fim = datetime(capturar_data)
    diferenca = data_fim - data_inicio
    dias = diferenca.days
    return dias


#caputura a escala
def capturar_escala():
    while True:
        try:
            escala = int(input(
            """
            +================================+
            | Escolha a sua escala inicial:   |
            |       1 - 08h as 16h            |
            |       2 - 16h as 24h            |
            |       3 - 24h as 08h            |
            +================================+
            """))
            if escala < 1 or escala > 3:
                print("")
                print("Escala invalida, selecione um intervalo entre 1 a 3")
            else:
                return escala    

        except ValueError:
            print("")
            print("Entrada inválida. Por favor, selecione um número entre 1 e 3.")

        
data_inicial = capturar_data()
escala_escolhida = capturar_escala()






numero_de_dias = dias
delta = datetime.timedelta(days=numero_de_dias)
data_folga = data_inicial + delta
     



#Print dos resultados capturados:
print("Data inicial da escala 1: ", data_inicial.strftime("%d/%m/%y"))
print("Vai folgar a partir do dia: ", data_folga.strftime("%d/%m/%y"))
print("Escala escolhida:", escala_escolhida)

















