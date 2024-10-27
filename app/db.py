import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='lady_store',
            user='root',  # seu usuário
            password='bro123'  # sua senha
        )
        if connection.is_connected():
            print("Conectado ao MySQL Server")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def get_all_clients():
    connection = create_connection()
    clients = []
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT CPF, identificador, nome, data_nascimento, email, telefone FROM Cliente")
        clients = cursor.fetchall()
        cursor.close()
        connection.close()
    return clients
