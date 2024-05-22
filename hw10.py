from gtts import gTTS
import playsound

tts=gTTS("안녕하세요 제 이름은 조경훈입니다. 잘 부탁드립니다", lang='ko')
tts.save("Hello.mp3")
playsound.playsound("Hello.mp3",True)
