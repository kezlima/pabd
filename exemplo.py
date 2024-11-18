from mysql.connector import (connection)

def connection():
    cnx=connection.MySQLConnection(
        user='root',
        password='labinfo',
        host='127.0.0.1',
        database='petshop'

    )
    return cnx

cnx= connection()

cursor=cnx.cursor(dicionario=True)

slq='SELECT * FROM animal'

cursor.execute(slq)

resultado=cursor.fetchall()

cursor.close()

cnx.close()

for tupla in resultado:
    print (f'id: {tupla['id']}, nome:{tupla['nome']}, raca:{tupla['raca']} ')