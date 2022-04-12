from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


class TelaApp(GridLayout):
    pass 

class Grid(App):
    def build(self):
        return TelaApp()

Grid().run()


