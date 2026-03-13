
from gtts import gTTS

def generate_voice(script):
    tts = gTTS(script)
    tts.save("audio.mp3")
