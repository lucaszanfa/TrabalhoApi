# SOBRE O FUNCIONAMENTO DO BACK-END

## APIProd

A API Produtos é uma APIRestful desenvolvida em Python com Flask (micro framework de desenvolvimento web no Python) e sqlite. 

Ela cria um banco de dados em sqlite chamado `banco.db` com uma tabela **Produtos** e implementa o CRUD dessa tabela. 

O código no arquivo `server.py` é um exemplo de um **aplicativo web usando o framework Flask** para uso acadêmico. 

Vamos entender as partes principais:

1. **Inicialização e Configuração**:
   
   - O Flask é inicializado com `app = Flask(__name__)`.
   - A configuração do banco de dados é definida com `app.config['SQLALCHEMY_DATABASE_URI']`.
   - O SQLAlchemy é configurado com `db = SQLAlchemy(app)`.

2. **Classe Produto**:
   
   - A classe `Produto` representa uma entidade (tabela) no banco de dados.
   - Ela possui as colunas `id`, `nome` e `preco`.
   - O método `serialize` converte os dados do produto em um formato JSON.

3. **Rotas**:
   
   - `/produtos` (GET): Retorna todos os produtos.
   - `/produtos/<int:produto_id>` (GET): Retorna um produto específico com base no ID.
   - `/produtos` (POST): Cria um novo produto com base nos dados enviados no corpo da requisição.
   - `/produtos/<int:produto_id>` (PUT): Atualiza os dados de um produto existente.
   - `/produtos/<int:produto_id>` (DELETE): Remove um produto do banco de dados.

4. **CORS (Cross-Origin Resource Sharing)**:
   
   - O CORS é configurado para permitir solicitações de origens específicas (por exemplo, `http://127.0.0.1:5500`).

5. **Execução**:
   
   - O aplicativo é executado com `app.run(debug=True)`.

Esse código cria um servidor web usado para gerenciar produtos em um banco de dados SQLite. Ele oferece endpoints para listar, criar, atualizar e excluir produtos.

Todo o código da APIRestful Produtos está no arquivo `server.py`, para executá-lo pela primeira vez, os pacotes a seguir devem ser instalados utilizando o pip:

```
pip install flask flask-sqlalchemy flask_cors
```

Para iniciar a API Produtos, execute server.py no prompt ou no terminal do VSCode:

```cmd
python server.py

* Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 100-995-094
```

Se a mensagem a seguir for exibida, a API estará disponível.

Para acessá-la, use um navegador ou o live server no VSCode:

```
http://127.0.0.1:5000/produtos
```

Se o banco de dados não existir, ele será criado com a tabela Produtos vazia e a resposta exibida será [] que representa uma um JSON vazio:

```
[ ]
```

Para inserir produtos na tabela, utilize uma ferramenta como Postman ou HTTPie.

# 
