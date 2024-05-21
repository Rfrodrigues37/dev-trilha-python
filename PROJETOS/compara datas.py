import datetime

# Função para calcular a diferença em dias entre duas datas
def dias_entre_datas(data1, data2):
    diferenca = data2 - data1
    return diferenca.days

# Função para verificar se um dia é folga
def verifica_folga(dias):
    # Calcular o dia de referência a partir da data inicial
    data_referencia = datetime.datetime.strptime("03/01/2024", "%d/%m/%Y").date()
    # Calcular o número de dias a partir da data de referência
    dias_desde_referencia = dias_entre_datas(data_referencia, datetime.datetime.now().date())
    # Calcular o padrão de folgas a cada 5 dias (dias 5, 10, 15, ...)
    if dias_desde_referencia % 5 in {0, 1, 2}:
        return True
    return False

while True:
    try:
        data_str = input("Digite a data (dd/mm/aaaa) ou 'sair' para terminar: ")
        if data_str.lower() == 'sair':
            break
        data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

        # Calcular a diferença em dias entre a data atual e a data informada
        dias = dias_entre_datas(datetime.datetime.now().date(), data)
        print(f"Quantidade de dias entre as duas datas: {dias}")

        # Verificar se o dia é folga
        if verifica_folga(dias):
            print("Dia de folga")
        else:
            print("Não é dia de folga")
    except ValueError:
        print("Formato inválido. Por favor, insira a data no formato dd/mm/aaaa.")

print("Programa encerrado.")




