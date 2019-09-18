from pydub import AudioSegment
sound = AudioSegment.from_mp3('mysong.mp3')

sound.export('myfile.wav', format='wav')
