from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
from kivy.properties import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.togglebutton import ToggleButton
import sys 

sys.path.insert(1, '../../')
from entidades import cliente
from repositorios import cliente_repositorio

class BotaoListagem(ToggleButton):
    def __init__(self, cliente_id, cliente_nome, cliente_idade, **kwargs):
        super(BotaoListagem, self).__init__(**kwargs)
        self.id_cliente = cliente_id
        self.cliente_nome = cliente_nome
        self.cliente_idade = cliente_idade
        self.text = self.cliente_nome + " " + self.cliente_idade
        self.group = 'clientes'   

    def _do_release(self, *args):
        TelaApp().cliente_selecionado(self.id_cliente)

class ExclusaoPopup(Popup):
    pass


class TelaApp(BoxLayout):
    id_cliente = 0 

    def __init__(self, **kwargs):
        super(TelaApp, self).__init__(**kwargs)
        self.listarClientes()

    def cliente_selecionado(self, id):
        TelaApp.id_cliente = id

    def editar_cliente(self):
        id = TelaApp.id_cliente
        nome = self.ids.nome.text #Obtem o texto escrito na variavel input
        idade = self.ids.idade.text #Obtem o texto escrito na variavel input
        novo_cliente = cliente.Cliente(nome, idade)
        cliente_repositorio.ClienteRepositorio.atualizar_cliente(id, novo_cliente)       

        #Limpa campos 
        self.ids.nome.text = ''
        self.ids.idade.text = ''

        #Atualiza lista de clientes 
        self.listarClientes()

    def cadastrarCliente(self):
        nome = self.ids.nome.text #Obtem o texto escrito na variavel input
        idade = self.ids.idade.text #Obtem o texto escrito na variavel input
        novo_cliente = cliente.Cliente(nome, idade)
        cliente_repositorio.ClienteRepositorio.inserir_cliente(novo_cliente)
        
        #Limpa campos 
        self.ids.nome.text = ''
        self.ids.idade.text = ''

        #Atualiza lista de clientes 
        self.listarClientes()

    def listarClientes(self):
        self.ids.clientes.clear_widgets()
        clientes = cliente_repositorio.ClienteRepositorio.listar_clientes()
        for i in clientes:
            id= str(i[0])
            nome = str(i[1])
            idade = str(i[2])

            #Criar um botão para cada cliente. Esse botão será inserido na scroll view chamado cliente
            self.ids.clientes.add_widget(BotaoListagem(id, nome, idade))

    def excluir_cliente(self):
        id = TelaApp.id_cliente
        
        popup = ExclusaoPopup()
        print (id)
        #usamos a função partial para passar outra função como parametro.
        #Precisamos fazer isso, pois não conseguimos passar o id do cliente para o nosso arquivo crud.kv. 
        popup.funcao = partial(self.remover, id) 
        popup.open() 

    def remover(self, id):
        
        cliente_repositorio.ClienteRepositorio.deletar_cliente(id)
        self.listarClientes()

class Crud(App):
    def build(self):
        return TelaApp()

Crud().run()
