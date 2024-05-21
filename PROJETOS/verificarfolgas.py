from datetime import datetime, timedelta

# Define a data de início da escala
data_inicio = datetime(2024, 1, 3)

# Define a escala de trabalho
escala = [4, 1, 4, 1, 4, 2]

# Função para verificar se a data é um dia de trabalho ou folga
def verificar_folga(data):
    dias_passados = (data - data_inicio).days
    indice_escala = sum(escala[:dias_passados % sum(escala)])
    return indice_escala % 7 < 4  # Dias < 4 são de trabalho, senão são folgas

# Testando a função com algumas datas
datas_teste = [
    datetime(2024, 1, 3),  # Dia de trabalho
    datetime(2024, 1, 7),  # Dia de folga
    datetime(2024, 2, 2),  # Dia de trabalho
    datetime(2024, 2, 3)   # Dia de folga
]

for data in datas_teste:
    if verificar_folga(data):
        print(f"{data.strftime('%d/%m/%Y')} é um dia de trabalho.")
    else:
        print(f"{data.strftime('%d/%m/%Y')} é um dia de folga.")

