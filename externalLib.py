from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
import networkx as nx
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(3,4)
G.add_edge(2,3)

class SimpleKivy(App):
    def build(self):
        b = BoxLayout()
        l = Label(text=str(nx.shortest_path(G,1,4)))
        textinput1 = TextInput(text=str(nx.shortest_path(G,1,4)))
        textinput1.bind(text=l.setter('text'))
        f = FloatLayout()
        s = Scatter()
        s.add_widget(l)
        f.add_widget(s)
        b.add_widget(f)
        b.add_widget(textinput1)
        return b
if __name__=="__main__":
    SimpleKivy().run()
