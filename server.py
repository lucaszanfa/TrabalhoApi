# pip install flask flask-sqlalchemy flask_cors

from flask import Flask, jsonify, request,  send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Inicialize o Flask e o SQLAlchemy:
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db = SQLAlchemy(app)

# Configure o CORS
CORS(app, origins=['http://127.0.0.1:5500']) 

# Classe que representa entidade no banco de dados: Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    # Adicione mais campos conforme necessário

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
        }

# Cria tabela no banco de dados
with app.app_context():
    db.create_all()

# Rota para Listar Todos os Produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.serialize() for produto in produtos])

# Rota para Listar um Produto Específico
@app.route('/produtos/<int:produto_id>', methods=['GET'])
def get_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if produto is None:
        return jsonify({'mensagem': 'Produto não encontrado'}), 404
    return jsonify(produto.serialize())

# Rota para Criar um Novo Produto
@app.route('/produtos', methods=['POST'])
def create_produto():
    dados = request.get_json()
    nome = dados['nome']
    preco = dados['preco']
    novo_produto = Produto(nome=nome, preco=preco)
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify(novo_produto.serialize()), 201

# Rota para Atualizar um Produto
@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def update_produto(produto_id):
    dados = request.get_json()
    produto = Produto.query.get(produto_id)
    if produto is None:
        return jsonify({'mensagem': 'Produto não encontrado'}), 404
    produto.nome = dados['nome']
    produto.preco = dados['preco']
    db.session.commit()
    return jsonify(produto.serialize())

# Rota para Deletar um Produto:
@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def delete_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if produto is None:
        return jsonify({'mensagem': 'Produto não encontrado'}), 404
    # Remova o produto do banco de dados
    db.session.delete(produto)
    db.session.commit()
    # Retorne uma resposta de sucesso
    return jsonify({'mensagem': 'Produto excluído com sucesso'}), 200

# Rota para a documentação da API (docAPIProd.html)
#@app.route('/')
#def serve_documentation():
    # Caminho para o arquivo docAPIProd.html
    #return send_file('docAPIProd.html')


if __name__ == '__main__':
    app.run(debug=True)
