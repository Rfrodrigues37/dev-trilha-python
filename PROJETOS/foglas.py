import datetime

def dias_entre_datas(data1, data2):
    diferenca = data2 - data1
    return diferenca.days

def verificar_folga(dias):
    # Folgas ocorrem nos dias que são múltiplos de 5 ou múltiplos de 15, incluindo 15 e 16.
    if dias % 5 == 0 or dias % 15 == 0 or dias % 15 == 1:
        return True
    return False

while True:
    try:
        data1_str = "03/01/2024"
        data2_str = input("Digite a segunda data (dd/mm/aaaa): ")
        data1 = datetime.datetime.strptime(data1_str, "%d/%m/%Y").date()
        data2 = datetime.datetime.strptime(data2_str, "%d/%m/%Y").date()
        break
    except ValueError:
        print("Formato inválido. Por favor, insira a data no formato dd/mm/aaaa.")

dias = dias_entre_datas(data1, data2)
print(f"Quantidade de dias entre as duas datas: {dias}")

if verificar_folga(dias):
    print(f"O dia {dias} é uma folga.")
else:
    print(f"O dia {dias} não é uma folga.")
