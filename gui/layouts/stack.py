from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


class TelaApp(StackLayout):
    pass 

class Stack(App):
    def build(self):
        return TelaApp()

Stack().run()


