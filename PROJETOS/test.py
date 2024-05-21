import datetime

# Função para calcular a diferença em dias entre duas datas
def dias_entre_datas(data1, data2):
    diferenca = data2 - data1
    return diferenca.days

# Função para verificar se um dia é folga
def verifica_folga(dias):
    if dias % 5 == 0 or dias % 15 == 0 or dias % 15 == 1:
        return True
    return False

# Loop para garantir que o usuário insira uma data válida
while True:
    try:
        data1_str = "03/01/2024"
        data2_str = input("Digite a segunda data (dd/mm/aaaa): ")
        data1 = datetime.datetime.strptime(data1_str, "%d/%m/%Y").date()
        data2 = datetime.datetime.strptime(data2_str, "%d/%m/%Y").date()
        break
    except ValueError:
        print("Formato inválido. Por favor, insira a data no formato dd/mm/aaaa.")

# Calcular a diferença em dias entre as duas datas
dias = dias_entre_datas(data1, data2)
print(f"Quantidade de dias entre as duas datas: {dias}")

# Verificar se o dia é folga
if verifica_folga(dias):
    print("Dia de folga")
else:
    print("Não é dia de folga")
