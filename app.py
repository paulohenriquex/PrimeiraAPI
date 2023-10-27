from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)
livros = [{}]


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    nome_livro = request.form['nome_livro']
    autor_livro = request.form['autor_livro']
    ano_livro = request.form['ano_livro']
    livros.append({'nome': nome_livro, 'autor': autor_livro, 'ano': ano_livro})
    return redirect(url_for('mostrar_livros'))


@app.route('/mostrar_livros')
def mostrar_livros():
    return render_template('livros.html', livros=livros)


@app.route('/alterar_livros')
def alterar_livros():
    return "Página de alteração de livros"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
