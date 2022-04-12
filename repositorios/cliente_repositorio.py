import MySQLdb
from fabricas import fabrica_conexao as fabrica_conexao


class ClienteRepositorio():
    # Essa classe não precisará de construtor pois ela não será instanciada. 
    @staticmethod
    def listar_clientes():
        # Cria uma conexão e instancia a conexão dentro de um objeto db
        db = fabrica_conexao.FabricaConexao.conectar()

        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM cliente")
            return cursor.fetchall()
        finally:    
            db.close()

    @staticmethod
    def inserir_cliente(cliente):
        # Cria uma conexão e instancia a conexão dentro de um objeto db        
        db = fabrica_conexao.FabricaConexao.conectar()

        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO cliente (nome,idade) VALUES (%s, %s)", (cliente.nome, cliente.idade))
        finally:
            db.close()

    @staticmethod
    def atualizar_cliente(idcliente, cliente):
        # Cria uma conexão e instancia a conexão dentro de um objeto db
        db = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = db.cursor()
            cursor.execute("UPDATE cliente SET nome=%s, idade=%s WHERE id=%s", (cliente.nome, cliente.idade, idcliente))
        finally:
            db.close()

    @staticmethod
    def deletar_cliente(idcliente):
        # Cria uma conexão e instancia a conexão dentro de um objeto db
        db = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = db.cursor()
            print (idcliente)
            cursor.execute("DELETE FROM cliente WHERE id=%s", [idcliente])
        except:
            raise
        finally:
            db.close()
