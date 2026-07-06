from flask import Flask, render_template, request
import mysql.connector

# Vincula as páginas
app = Flask(__name__)

# Cria conexão com o mySQL
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1',
    'ssl_disabled': True
}

# Criação de rota para o arquivo HTML principal
@app.route('/')
def indexRota():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def criar_cadastro():
    # Recebe os dados do formulário
    try:
        cpf = request.form['cpf']
        primeiro_nome = request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']
        idade = request.form['idade']

        # Criar conexão com o banco de dados
        conexao = mysql.connector.connect(**bd_config)
        
        # Levar instruções SQL do Python até o banco de dados
        curso = conexao.cursor()
        
        query = "INSERT INTO cliente1 (CPF, PRIMEIRO_NOME, SOBRENOME, IDADE) VALUES (%s, %s, %s, %s)"
        dados = (cpf, primeiro_nome, sobrenome, idade)
        
        # Executando o código corretamente
        curso.execute(query, dados)
        
        # Salvando as alterações
        conexao.commit()
        
        # Fechando cursor e conexão
        curso.close()
        conexao.close()
        
        # Correção nas aspas do href
        return f"<h3> Cliente {primeiro_nome} cadastrado com sucesso!</h3><a href='/'> Voltar </a>"

    except mysql.connector.Error as erro:
        return f'Erro ao gravar no banco de dados: {erro}'

if __name__ == '__main__':
    app.run(debug=True)