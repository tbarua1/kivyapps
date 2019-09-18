from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('mysong.mp3')
play(sound)

