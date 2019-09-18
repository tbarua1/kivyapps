from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class MyFirstKivyApp(App):
    def build(self):
        superBox= BoxLayout(orientation='vertical')
        horizontalBox   = BoxLayout(orientation='horizontal')
        button1= Button(text="One")
        button2= Button(text="Two")
        horizontalBox.add_widget(button1)
        horizontalBox.add_widget(button2)
        verticalBox= BoxLayout(orientation='vertical')
        button3= Button(text="Three")
        button4= Button(text="Four")
        verticalBox.add_widget(button3)
        verticalBox.add_widget(button4)
        superBox.add_widget(horizontalBox)
        superBox.add_widget(verticalBox)
        return superBox
if __name__=="__main__":
    MyFirstKivyApp().run()
