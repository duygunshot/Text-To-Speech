from gtts import gTTS
from pygame import mixer
import time
text = "Enter text here"
obj = gTTS(text=text, lang= "en",slow= "False" )
obj.save("soundtext.mp3")
mixer.init()
mixer.music.load("soundtext.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)