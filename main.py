from time import sleep
from gtts import gTTS
import speech_recognition as srLib
from playsound import playsound


class Saito:
    def __init__(self):
        self.nome = "Saito Shion Cipriano"

        if self.lerUsuario() == "":
            self.gravarUsuario()

        self.usuario = self.lerUsuario()

        welcome = f"Seja bem vindo(a) novamente {self.user}!"
        print(welcome)
        self.falar(welcome)

        self.inicializar(self.usuario)

    def inicializar(self, nome):
        pass

    def gravarUsuario(self):
        self.boas_vindas_txt = open("./db/Boas vindas.txt", "rt", encoding="utf-8")
        print(self.boas_vindas_txt.read())
        self.boas_vindas_txt.close()

        self.user_txt = open("./db/User.txt", "wt", encoding="utf-8")
        user = self.ouvir(frase="Qual é o seu nome?")
        print(self.user_txt.write(user))
        self.user_txt.close()

    def lerUsuario(self):
        self.user_txt = open("./db/User.txt", "rt", encoding="utf-8")
        self.user = self.user_txt.read()
        self.user_txt.close()

        return self.user

    def ouvir(self, frase = "*Ouvindo*", erro = "Desculpa, não entendi direito."):
        mic = srLib.Recognizer()

        with srLib.Microphone() as gravacao:
            try:
                mic.adjust_for_ambient_noise(gravacao)
                print(frase)
                sleep(1)
                audio = mic.listen(gravacao)
                texto = mic.recognize_google(audio, language="pt-BR")
                print(texto)
                return texto
            except srLib.UnknownValueError:
                print(erro)

    def falar(self, texto):
        try:
            tts = gTTS(texto, lang="pt-BR")
            localAudio = "./db/temp_audio.mp3"
            tts.save(localAudio)
            playsound(localAudio)
        except:
            print(f"""Erro no código""")

    def abrirSoftware(self):
        pass

    def abrirPagina(self):
        pass

if __name__ == '__main__':
    Saito()