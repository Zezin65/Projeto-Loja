# Biblioteca de conexão com o banco de dados
import mysql.connector
# Biblioteca de erro do banco de dados
import mysql.connector.errors

def criarConexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password="",
            database="fabrica"
        )
        return conexao
    except mysql.connector.errors.IntegrityError as error:
        print("Erro de integridade: ", error)
        return None     
def login(usuario, senha):
    conexao = criarConexao()

    if conexao is None:
        return False
    else:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM usuarios where idUsuarios = {usuario} and senha = {senha};")
        resultado = cursor.fetchall()
        
        usuario = {}

        if len(resultado) > 0:
            print(resultado)
            usuario['id'] = resultado[0][0]
            usuario['nome'] = resultado[0][1]
            usuario['funcao'] = resultado[0][2]
            usuario['senha'] = resultado[0][3]
        else:
            print("Usuário não encontrado")
            usuario["erro"] = True

        print(resultado)
    
        cursor.close()
        conexao.close()
        
        return usuario

login(1, 300315)
    