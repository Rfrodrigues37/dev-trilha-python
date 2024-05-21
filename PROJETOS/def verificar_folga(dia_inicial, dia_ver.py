from datetime import datetime, timedelta

def calcular_folga(data_inicio, data_verificar):
    # Convertendo as datas de string para datetime
    data_inicio_dt = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_verificar_dt = datetime.strptime(data_verificar, '%d/%m/%Y')

    # Calculando o número de dias entre as datas
    dias_passados = (data_verificar_dt - data_inicio_dt).days

    # Calculando o número de semanas completas
    semanas_completas = dias_passados // 7

    # Calculando o dia na semana para a data de verificação
    dia_semana_verificar = data_verificar_dt.weekday()

    # Verificando se está de folga
    if semanas_completas % 3 == 2:  # 4 dias de trabalho e 2 dias de folga
        if dia_semana_verificar == 5 or dia_semana_verificar == 6:  # sábado ou domingo
            return True
    else:  # 4 dias de trabalho e 1 dia de folga
        if dia_semana_verificar == 4:  # sexta-feira
            return True
    
    return False

# Exemplo de uso
data_inicio = input("Digite a data de início da escala (no formato DD/MM/AAAA): ")
data_verificar = input("Digite a data que deseja verificar (no formato DD/MM/AAAA): ")

if calcular_folga(data_inicio, data_verificar):
    print("Você está de folga nessa data.")
else:
    print("Você está trabalhando nessa data.")

