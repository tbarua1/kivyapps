import time
import wave

from kivy.app import App
from kivy.uix.button import Button

frames = []

def mic_callback(buf):
    print ('got', len(buf))
    frames.append(buf)
def bcallback(instance):
    sdpath = App.get_running_app().user_data_dir
    print('saving2')
    mic = input(callback=mic_callback)
    mic.start()

    frames.append(mic.poll())
    time.sleep(5)

    mic.stop()

    wf = wave.open(sdpath+"test.wav", 'wb')
    wf.setnchannels(mic.channels)
    wf.setsampwidth(2)
    wf.setframerate(mic.rate)
    wf.writeframes(b''.join(frames))
    wf.close()

class MyApp(App):
    def build(self):

        btn1 = Button(text='Audio Record')
        btn1.bind(on_press=bcallback)
        return btn1
if __name__ == '__main__':
    MyApp().run()
