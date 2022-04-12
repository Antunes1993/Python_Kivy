from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

class Principal(BoxLayout):
    texto_principal = StringProperty('Eu sou uma label')
    tamanho_texto_principal = NumericProperty(30)

    def teste(self):
        self.texto_principal = "Fui clicado"
        self.tamanho_texto_principal += 20

class Teste(App):
    #Método que monta e inicializa a aplicação.
    def build(self):
        return Principal()
    
Teste().run()




