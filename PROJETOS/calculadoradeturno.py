import datetime

def verificar_folga(primeiro_dia_trabalho, horario_primeiro_dia):
    # Define a escala de trabalho (dias de trabalho seguidos e dias de folga)
    escala_trabalho = [4, 1, 4, 1, 4, 2]  # Exemplo: 4x1 4x1 4x2

    # Calcula a data da próxima folga
    data_proxima_folga = calcular_proxima_folga(primeiro_dia_trabalho, escala_trabalho)

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

            # Calcula o próximo dia de trabalho e em qual horário
            proximo_dia_trabalho, horario_proximo_dia = calcular_proximo_dia_trabalho(data_proxima_folga, horario_primeiro_dia, escala_trabalho)
            print(f"Seu próximo dia de trabalho será em {proximo_dia_trabalho.strftime('%d/%m/%Y')} no horário {horario_proximo_dia}")

            # Sai do loop
            break

        except ValueError:
            print("Formato de data inválido. Digite a data no formato DD/MM/AAAA.")

def calcular_proxima_folga(primeiro_dia_trabalho, escala_trabalho):
    # Inicializa um contador para controlar os dias de trabalho e folga
    contador = 0

    # Percorre a escala de trabalho para encontrar a data da próxima folga
    for dias in escala_trabalho:
        # Adiciona os dias da escala ao contador
        contador += dias

        # Calcula a data da próxima folga
        data_folga = primeiro_dia_trabalho + datetime.timedelta(days=contador)

        # Verifica se a data da próxima folga é um sábado (dia de folga na escala)
        if data_folga.weekday() == 5:  # 5 representa o sábado
            return data_folga

def calcular_proximo_dia_trabalho(data_atual, horario_atual, escala_trabalho):
    # Encontra o próximo horário de trabalho na escala
    proximo_horario_index = (horario_atual - 1 + 1) % len(escala_trabalho) + 1

    # Encontra a próxima data de trabalho na escala
    proximo_dia_index = (horario_atual - 1 + 1) // len(escala_trabalho)
    while True:
        if proximo_horario_index > len(escala_trabalho):
            proximo_dia_index += 1
            proximo_horario_index = 1
        if escala_trabalho[proximo_horario_index - 1] > 0:
            break
        proximo_horario_index += 1

    # Calcula a próxima data de trabalho e horário
    dias_trabalho = sum(escala_trabalho[:proximo_horario_index - 1]) + proximo_dia_index * sum(escala_trabalho)
    data_proximo_trabalho = data_atual + datetime.timedelta(days=dias_trabalho)
    horario_proximo_trabalho = proximo_horario_index

    return data_proximo_trabalho, horario_proximo_trabalho

# Exemplo de uso
data_primeiro_dia_trabalho = datetime.date(2024, 1, 3)  # 03/01/2024
horario_primeiro_dia = 1  # Horário 1: 08h as 16h

verificar_folga(data_primeiro_dia_trabalho, horario_primeiro_dia)

