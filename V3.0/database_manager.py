import mysql.connector
from mysql.connector import Error

def criar_conexao():
    """Estabelece a conexão com o banco de dados MySQL"""
    try:
        conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "agenda_db"
            
        )
        if conexao.is_connected():
            return conexao
    
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
def inicializacao_banco():

    conexao = criar_conexao()
    if conexao:
        cursor= conexao.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS tarefas(
            id INT AUTO_INCREMENT PRIMARY KEY,
            acao VARCHAR(100) NOT NULL,
            data_tarefa VARCHAR(10) NOT NULL,
            hora_tarefa VARCHAR(5) NOT NULL,
            status ENUM('Pendente', 'Em andamento','Concluída') DEFAULT 'Pendente',
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                );"""
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Banco de dados pronto para uso!")

def buscar_tarefas():

    conexao =  criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary= True)# Pega todas as linhas
            query = "SELECT id, acao, data_tarefa, hora_tarefa, status FROM  tarefas ORDER BY data_tarefa ASC"
            cursor.execute(query)
            resultado = cursor.fetchall()   # Pega todas as linhas 
            return resultado
        
        except Error as e: 
            print(f"Erro ao buscar dados: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()
    return [] 