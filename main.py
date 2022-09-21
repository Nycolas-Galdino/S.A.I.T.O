from time import sleep
import pyttsx3
import speech_recognition as srLib
import webbrowser as wb


class Saito:
    def __init__(self):
        self.nome = "Saito Shion Cipriano"
        self.microfone = None
        self.volume = 0.5

        if self.lerUsuario() == "":
            self.gravarUsuario()

        self.usuario = self.lerUsuario()

        welcome = f"Olá novamente {self.user}!"
        self.falar(welcome)
        self.inicializar()

    def inicializar(self):
        for i in range(5):
            frase = self.ouvir()

            if i == 5:
                self.falar("Notei uma certa inatividade no sistema, irei encerrar por agora, okay? Até mais!")

            if "fechar" in frase:
                self.falar("Tudo bem, fico por aqui então! Até logo!")
                break

            if "pesquisar" in frase:
                self.abrirPagina(frase.replace("pesquisar",""))
                sleep(5)
                i=0

    def gravarUsuario(self):
        import config
        config

        self.user_txt = open("./db/User.txt", "wt", encoding="utf-8")
        user = self.ouvir()
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
                return texto
            except srLib.UnknownValueError:
                print(erro)

    def falar(self, texto):
        print(texto)
        try:
            if self.microfone is None:
                self.microfone = self.configurarMicrofone()

                #Velocidade do som
            if len(texto) <= 50:
                self.voz.setProperty("rate",200)
            elif len(texto) <= 100:
                self.voz.setProperty("rate",250)
            elif len(texto) <= 200:
                self.voz.setProperty("rate",300)
            else:
                self.voz.setProperty("rate", 350)

                #Volume
            if self.volume == 1:
                self.falar("O volume está no máximo")

            if self.volume == 0.25:
                self.falar("O volume está no mínimo")

            if texto == "Aumentar o volume" and self.volume < 1:
                self.volume +=  0.25
                self.falar("O volume está em {}%".format(100*(self.volume/1)))

            if texto == "Diminuir o volume" and self.volume > 0.25:
                self.volume -=  0.25
                self.falar("O volume está em {}%".format(100*(self.volume/1)))

            self.voz.setProperty("voice",self.microfone)
            self.voz.setProperty("volume",self.volume)
            self.voz.say(texto)
            self.voz.runAndWait()
        except:
            print(f"""Erro ao falar""")

    def configurarMicrofone(self):
        self.voz = pyttsx3.init("sapi5")
        self.vozes = self.voz.getProperty("voices")
        x = 0

        for i in self.vozes:
            if "Saito" in str(i):
                break
            x += 1

        return self.vozes[x].id

    def abrirSoftware(self):
        pass

    def abrirPagina(self, pagina):
        wb.open(fr"www.google.com/search?q={pagina}".replace(" ","%20"))
        self.falar("Abrino pesquisa na web")

if __name__ == '__main__':
    Saito()