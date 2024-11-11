from flask import Flask
from mysql.connector import (connection)
from flask import request
from flask import render_template


app=Flask(__name__)

@app.route("/")

def teste():
    return render_template('index.html')


@app.route('/adicao', methods=['POST'])
def adicionar():
    cnx=connection.MySQLConnection(
        user='root',
        password='labinfo',
        host='127.0.0.1',
        database='petshop'

    )

    nome=request.form['nome']
    raca=request.form['raca']
    
    print(nome)
    print(raca)


    sql="INSERT INTO animal (nome, raca) VALUES (%s, %s)"
    tupla=(nome,raca)
    cursor=cnx.cursor()
    cursor.execute(sql, tupla)
    cnx.commit()


    cnx.close()
    return 'sucesso'

@app.route('/apagar')
def apagar():
    cnx=connection.MySQLConnection(
        user='root',
        password='labinfo',
        host='127.0.0.1',
        database='petshop'

    )
    sql="DELETE FROM animal where id=%s"
    tupla=(2,)
    cursor=cnx.cursor()
    tupla(2,)
    cursor.execute(sql, tupla)
    cnx.commit()


    cnx.close()
    return 'sucesso'


