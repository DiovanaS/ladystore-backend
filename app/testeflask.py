from flask import Flask, jsonify
from db import create_connection, get_all_clients  # Importação correta

app = Flask(__name__)

@app.before_request
def init():
    connection = create_connection()
    if connection:
        print("Conexão estabelecida com o banco de dados.")
        connection.close()
    else:
        print("Falha ao conectar com o banco de dados.")

@app.route('/')
def index():
    return "Bem-vindo ao aplicativo Flask!"

@app.route('/clientes', methods=['GET'])
def clientes():
    clients = get_all_clients()  # Esta linha deve funcionar corretamente
    if clients:
        return jsonify(clients), 200
    else:
        return jsonify({"message": "Nenhum cliente encontrado."}), 404

if __name__ == '__main__':
    app.run(debug=True)
