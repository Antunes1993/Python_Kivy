import MySQLdb, configparser

class FabricaConexao():
    @staticmethod
    def conectar():
        config = configparser.ConfigParser()
        config.read('../../config.ini')
        db = MySQLdb.connect(user=config['DATABASE']['user'],
                             passwd=config['DATABASE']['passwd'],
                             db=config['DATABASE']['db'],
                             port=int(config['DATABASE']['port']),
                             autocommit=config['DATABASE']['autocommit'])
        return db



