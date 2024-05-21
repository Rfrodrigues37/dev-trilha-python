import datetime

def verificar_folga(data_primeiro_dia_trabalho):
    # Define a escala de trabalho (dias de trabalho seguidos e dias de folga)
    escala_trabalho = [4, 1, 4, 1, 4, 2]  # Exemplo: 4x1 4x1 4x2

    # Calcula a data da próxima folga
    data_proxima_folga = calcular_proxima_folga(data_primeiro_dia_trabalho, escala_trabalho)

    # Captura a data fornecida pelo usuário para verificar a folga
    while True:
        try:
            data_verificacao = input("Digite a data que deseja verificar (DD/MM/AAAA): ")
            dia, mes, ano = map(int, data_verificacao.split('/'))
            data_verificacao = datetime.date(ano, mes, dia)

            # Verifica se a data de verificação está na escala de folga
            if data_verificacao == data_proxima_folga:
                print("Você está de folga nessa data.")
            else:
                print("Você não está de folga nessa data.")

            # Sai do loop
            break

        except ValueError:
            print("Formato de data inválido. Digite a data no formato DD/MM/AAAA.")

def calcular_proxima_folga(data_primeiro_dia_trabalho, escala_trabalho):
    # Inicializa um contador para controlar os dias de trabalho e folga
    contador = 0

    # Percorre a escala de trabalho para encontrar a data da próxima folga
    for dias in escala_trabalho:
        # Adiciona os dias da escala ao contador
        contador += dias

        # Calcula a data da próxima folga
        data_folga = data_primeiro_dia_trabalho + datetime.timedelta(days=contador)

        # Verifica se a data da próxima folga é um sábado (dia de folga na escala)
        if data_folga.weekday() == 5:  # 5 representa o sábado
            return data_folga

# Exemplo de uso
while True:
    try:
        data_primeiro_dia_trabalho = input("Digite a data do primeiro dia de trabalho da escala (DD/MM/AAAA): ")
        dia, mes, ano = map(int, data_primeiro_dia_trabalho.split('/'))
        data_primeiro_dia_trabalho = datetime.date(ano, mes, dia)
        break
    except ValueError:
        print("Formato de data inválido. Digite a data no formato DD/MM/AAAA.")

verificar_folga(data_primeiro_dia_trabalho)
