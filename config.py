import os
from time import sleep
import pyttsx3

tts = pyttsx3.init("sapi5")

voices = tts.getProperty("voices")
x=0

print("Estou configurando minha voz...")
print("Por favor, aceite as permissões para cadastrar minha voz.")
sleep(3)

for i in voices:
    if "Saito" in str(i):
        print(i)
        break

    if i == voices[len(voices) - 1]:
        os.system("Saito.reg")
        x += 1
        break

    x += 1

tts.setProperty("voice", voices[x].id)
print("Pronto! Agora você consegue me ouvir melhor!")
tts.say("Pronto! Agora você consegue me ouvir melhor!")
tts.runAndWait()

boasVindas = """Olá, meu nome é Saito, prazer em lhe conhecer!

Sou uma IA desenvolvida para lhe fornecer o maior auxílio possível.

Estou programado para ouvir você através de seu MICROFONE, então, vamos lá!

Por favor, me diga seu nome!"""

print(boasVindas)
tts.say(boasVindas)
tts.runAndWait()
