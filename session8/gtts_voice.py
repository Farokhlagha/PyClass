# pip install gtts
import gtts

my_text = "I am a student of python programmer"

x = gtts.gTTS(my_text, lang="en", slow=False)
x.save("session8/voice.mp3")


print(gtts.lang.tts_langs()) # which language is suported