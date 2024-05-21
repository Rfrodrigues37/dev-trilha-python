import datetime

def verificar_folga():
    # Define a escala de trabalho (dias de trabalho seguidos e dias de folga)
    escala_trabalho = [4, 1, 4, 1, 4, 2]  # Exemplo: 4x1 4x1 4x2

    # Obtém a data de hoje
    hoje = datetime.date.today()

    # Calcula a data da próxima folga
    data_proxima_folga = calcular_proxima_folga(hoje, escala_trabalho)

    # Captura a data fornecida pelo usuário
    while True:
        try:
            data_digitada = input("Digite a data no formato DD/MM/AAAA: ")
            dia, mes, ano = map(int, data_digitada.split('/'))
            data_inserida = datetime.date(ano, mes, dia)

            # Verifica se a data inserida está na escala de folga
            if data_inserida == data_proxima_folga:
                print("Você está de folga nessa data.")
            else:
                print("Você não está de folga nessa data.")

            # Sai do loop
            break

        except ValueError:
            print("Formato de data inválido. Digite a data no formato DD/MM/AAAA.")

def calcular_proxima_folga(data_atual, escala_trabalho):
    # Inicializa um contador para controlar os dias de trabalho e folga
    contador = 0

    # Percorre a escala de trabalho para encontrar a data da próxima folga
    for dias in escala_trabalho:
        # Adiciona os dias da escala ao contador
        contador += dias

        # Calcula a data da próxima folga
        data_folga = data_atual + datetime.timedelta(days=contador)

        # Verifica se a data da próxima folga é um sábado (dia de folga na escala)
        if data_folga.weekday() == 5:  # 5 representa o sábado
            return data_folga

# Exemplo de uso
verificar_folga()
