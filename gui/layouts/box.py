from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


class TelaApp(BoxLayout):
    pass 

class Box(App):
    def build(self):
        return TelaApp()

Box().run()