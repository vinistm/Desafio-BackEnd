import sqlite3
con = sqlite3.connect("CNAB.db")
c = con.cursor()

def table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS COMPANY (
            tipo,data,valor,cpf,cartao,hora,dono,loja
            )""")

table()

def insert_values(data_list):
    for data in data_list:
        query = f"""
        INSERT INTO COMPANY (tipo,data,valor,cpf,cartao,hora,dono,loja) VALUES
         ({data[0]},{data[1]},{data[2]},{data[3]},"{data[4]}",{data[5]},"{data[6]}","{data[7]}")"""
        select = f"""SELECT * FROM COMPANY"""
    c.execute(query)
    print(c.execute(select))

    con.commit()

