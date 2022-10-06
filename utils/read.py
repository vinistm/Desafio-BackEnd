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

                data = (tipo, date, valor_convertido, cpf, cartao, hora, dono, loja)
                list_data.append(data)

            return list_data
