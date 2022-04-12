from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


class TelaApp(FloatLayout):
    pass 

class Float(App):
    def build(self):
        return TelaApp()

Float().run()