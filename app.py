import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'AC01'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  cpf = request.form['cpf']
  endereco = request.form['endereco']
  if nome and cpf and endereco:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_ac (nome, cpf, endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
    conn.commit()
    return 'Aluno cadastrado!'
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome, cpf, endereco from tbl_ac')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
