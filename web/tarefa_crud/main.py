import pymysql
from app import app
from table import Results
from db_config import mysql
from flask import flash, render_template, request, redirect

@app.route('/new_tarefa')
def add_tarefa_view():
	return render_template('add.html')
		
@app.route('/add', methods=['POST'])
def add_tarefa():
	try:		
		_titulo = request.form['inputTitulo']
		_descricao = request.form['inputDescricao']
		_status = request.form['inputStatus']
		if _titulo and _descricao and _status and request.method == 'POST':
			sql = "INSERT INTO tarefa(tarefa_titulo, tarefa_descricao, tarefa_status) VALUES(%s, %s, %s)"
			data = (_titulo, _descricao, _status,)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Tarefa adicionada com sucesso!')
			return redirect('/')
		else:
			return 'Erro enquanto adicionava a tarefa'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def list_tarefas():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tarefa")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('list.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/edit/<int:id>')
def edit_view(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tarefa WHERE tarefa_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Erro ao acessar a tarefa #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/update', methods=['POST'])
def update_tarefa():
	try:		
		_titulo = request.form['inputTitulo']
		_descricao = request.form['inputDescricao']
		_status = request.form['inputStatus']
		_id = request.form['id']
		if _titulo and _descricao and _status and _id and request.method == 'POST':
			sql = "UPDATE tarefa SET tarefa_titulo=%s, tarefa_descricao=%s, tarefa_status=%s WHERE tarefa_id=%s"
			data = (_titulo, _descricao, _status, _id,)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Tarefa alterada com sucesso!')
			return redirect('/')
		else:
			return 'Erro ao alterar os dados da tarefa.'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>')
def delete_tarefa(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tarefa WHERE tarefa_id=%s", (id,))
		conn.commit()
		flash('Tarefa deletada com sucesso!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
if __name__ == "__main__":
	app.run(port=5000)
