from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 2,
        'titulo': 'O Hobbit',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 3,
        'titulo': 'O Silmarillion',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 4,
        'titulo': 'A Sociedade do Anel',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 5,
        'titulo': 'As Duas Torres',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 6,
        'titulo': 'O Retorno do Rei',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 7,
        'titulo': 'O Silmarillion',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 8,
        'titulo': 'O Silmarillion',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 9,
        'titulo': 'O Silmarillion',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    },
    {
        'id': 10,
        'titulo': 'O Silmarillion',
        'autor': 'J. R. R. Tolkien',
        'editora': 'HarperCollins Brasil',
    }

]


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def obterLivroPorID(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        



app.run(port=5000, host='localhost', debug=True)
