from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
class IconButton(ButtonBehavior, Image):
    def on_press(self):
        print("on_press")
    def state_changed(*args):
        print('state changed')
        # button = Button()
        # button.bind(state=state_changed)
class AddingBehaviorApp(App):
    def build(self):
        return IconButton()
if __name__=='__main__':
    AddingBehaviorApp().run()
