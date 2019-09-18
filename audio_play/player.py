from kivy.app import App
from kivy.uix.button import Button
from playsound import playsound


def bcallback():

    playsound('mysong.mp3')

class MyApp(App):
    def build(self):
        btn1 = Button(text='Audio Record')
        btn1.bind(on_press=bcallback)
        return btn1
if __name__ == '__main__':
    MyApp().run()
