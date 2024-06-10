from datetime import datetime, timedelta

def gerar_sequencia_folga(n):
    sequencia_folga = []
    valor_atual = 5
    
    for i in range(n):
        sequencia_folga.append(valor_atual)
        
        if (i + 1) % 5 == 0:
            valor_atual += 1
        else:
            valor_atual += 5
    
    return sequencia_folga

def calcular_dias_passados(data_inicial, data_final):
    delta = data_final - data_inicial
    return delta.days

def verificar_folga(data):
    data_referencia = datetime(2024, 1, 2)
    dias_passados = calcular_dias_passados(data_referencia, data)
    
    # Gere uma sequência grande o suficiente para cobrir os dias necessários
    sequencia_folga = gerar_sequencia_folga(dias_passados + 1)
    
    # Verifique se o dia em questão está na sequência de folga
    return dias_passados in sequencia_folga

# Insira a data para verificar
data_input = input("Digite a data no formato dd/mm/aaaa: ")
data = datetime.strptime(data_input, "%d/%m/%Y")

if verificar_folga(data):
    print(f"A data {data_input} é um dia de folga.")
else:
    print(f"A data {data_input} não é um dia de folga.")
