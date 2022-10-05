from tabulate import tabulate
def read_text(filepath: str) -> list[dict]:
    with open("CNAB.txt", 'r',  encoding="utf-8") as file:
        list_data = []
        for line in file:
            tipo = line[0]
            date = line[1:9]
            valor = line[9:19]
            cpf = line[19:30]
            cartao = line[30:42]
            hora = line[42:48]
            # fomato_hora = {}
            dono = line[48:62]
            loja = line[62:81]
            converter_valor = int(valor) * 100
            data = (tipo, date,converter_valor,cpf, cartao, hora, dono, loja)
            
            list_data.append(data)

        print(tabulate(list_data,headers=['Tipo','data','valor','cpf','cartao','hora','dono','loja']))
        return list_data
# for row in read_text("select * from COMPANY"):
#     print(row)