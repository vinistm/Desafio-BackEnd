def read_file(filepath: str) -> list[dict]:
    with open(filepath, 'r',  encoding="utf-8") as file:

            list_data = []

            Linhas = file.readlines()
            for content in Linhas:
                tipo = content[0]
                date = content[1:9]
                valor = content[9:19]
                cpf = content[19:30]
                cartao = content[30:42]
                hora = content[42:48]
                dono = content[48:62]
                loja = content[62:81]


                valor_convertido = int(valor) * 100
                # list_hora = list(hora)
                # lista= list(date)
                # data_format = f"{lista[0]}{lista[1]}{lista[2]}{lista[3]}-{lista[4]}{lista[5]}-{lista[6]}{lista[7]}"
                # print(data_format)
                # hora_format = f"{list_hora[0]} {list_hora[1]}:{list_hora[2]} {list_hora[3]}:{list_hora[4]}{list_hora[5]}"

                data = (tipo, date, valor_convertido, cpf, cartao, hora, dono, loja)
                list_data.append(data)

            return list_data
