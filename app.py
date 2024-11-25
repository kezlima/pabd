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
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'

    )

    nome=request.form['nome']
    raca=request.form['raca']
    
    print(nome)
    print(raca)


    sql="INSERT INTO animal (nome, raca) VALUES ( %s, %s)"
    tupla=(nome,raca)
    cursor=cnx.cursor()
    cursor.execute(sql, tupla)
    cnx.commit()


    cnx.close()
    return 'sucesso'

'''@app.route('/apagar')
def apagar():
    cnx=connection.MySQLConnection(
        user='root',
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'

    )
    sql="DELETE FROM animal where id=%s"
    tupla=(2,)
    cursor=cnx.cursor()
    cursor.execute(sql, tupla)
    cnx.commit()


    cnx.close()
    return 'sucesso'
'''
@app.route('/exibir', methods=['GET', 'POST'])
def exibir():
    cnx=connection.MySQLConnection(
        user='root',
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'

    )

  
    cursor=cnx.cursor()
    
    sql=("SELECT id, nome, raca FROM animal")

    cursor.execute(sql)

    mens= cursor.fetchall()

    cursor.close()  
    cnx.close()

    return render_template("animais.html", animal=mens)
    

@app.route('/apagar/<int:id>', methods=['POST'])
def apagar(id):
    cnx=connection.MySQLConnection(
        user='root',
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'

    )

  
    cursor=cnx.cursor()
    sql=("SELECT id, nome, raca FROM animal")
    cursor.execute(sql)
    mens= cursor.fetchall()

    cursor.execute("DELETE FROM animal WHERE id = %s", (id,))
    cnx.commit() 
    print('apagou')  
    

    cursor.close()  
    cnx.close()

    return render_template("animais.html", animal=mens)
    
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    cnx=connection.MySQLConnection(
        user='root',
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'

    )
    nome = request.form['nome']
    raca = request.form['raca']
  
    cursor=cnx.cursor()
    cursor.execute("""
            UPDATE animal
            SET nome = %s, raca = %s
            WHERE id = %s
        """, (nome, raca, id))
    
    cnx.commit()
    print('atualizou')  
    
    
    sql=("SELECT id, nome, raca FROM animal")
    cursor.execute(sql)
    mens= cursor.fetchall()
    
    cursor.close()  
    cnx.close()

    return render_template("animais.html", animal=mens)
    
@app.route('/atualizar/<int:id>', methods=['GET'])
def exibir_formulario_atualizacao(id):
    cnx = connection.MySQLConnection(
        user='root',
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'
    )
    cursor = cnx.cursor()
    
    # Busca o produto pelo ID
    cursor.execute("SELECT id, nome, raca FROM animal WHERE id = %s", (id,))
    dados = cursor.fetchone()
    
    cursor.close()
    cnx.close()
    
    # Renderiza a página de atualização com os dados do produto
    return render_template('atualizar.html', cachorro=dados)


@app.route('/adicao', methods=['GET', 'POST'])
def quantidade():
    cnx = connection.MySQLConnection(
        user='root',
        password='mdl587905',
        host='127.0.0.1',
        database='petshop'
    )

    cursorQ = cnx.cursor()
    sqlQuantidade = 'SELECT raca FROM animal'

    cursorQ.execute(sqlQuantidade)
    resultadoQuantidade = cursorQ.fetchone()
    print(resultadoQuantidade)

    cursorQ.close()
    cnx.close()

    return render_template('index.html',lQnt = resultadoQuantidade)
    

    
