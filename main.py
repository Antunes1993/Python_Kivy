import MySQLdb, entidades.cliente as cliente
from fabricas import fabrica_conexao as fabrica_conexao
from repositorios.cliente_repositorio import ClienteRepositorio

db = fabrica_conexao.FabricaConexao.conectar()

print("Conexão realizada: ", type(db))
cursor = db.cursor()
cliente = cliente.Cliente("Eduardo", 19)
ClienteRepositorio.inserir_cliente(cliente)
ClienteRepositorio.listar_clientes()

#Encerra uma conexão
db.close()
