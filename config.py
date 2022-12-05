import os
from time import sleep
import pyttsx3

tts = pyttsx3.init("sapi5")

print("Estou configurando minha voz...")

def verificarVozes():
    x=0
    voices = tts.getProperty("voices")

    for i in voices:
        if "Saito" in str(i):
            return x

        x += 1

if verificarVozes() == None:
    print("Por favor, aceite as permissões para cadastrar minha voz.")
    sleep(5)
    os.system("Saito.reg")

sleep(2)

id = int(verificarVozes())
voices = tts.getProperty("voices")

tts.setProperty("voice", voices[id].id)
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
