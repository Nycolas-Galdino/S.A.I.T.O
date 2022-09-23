import json
import os
from time import sleep
import pyttsx3
import pywhatkit as pywhatkit
import speech_recognition as srLib
import webbrowser as wb
import wikipedia


class Saito:
    def __init__(self):
        self.nome = "Saito Shion Cipriano"
        self.microfone = None
        self.volume = 0.5

        if self.lerUsuario() == "":
            self.gravarUsuario()

        self.usuario = self.lerUsuario()

        self.falar(f"Olá novamente {self.user}")

        with open("db/Dicionário.json","r", encoding="utf-8") as dicionario:
            self.dados = json.load(dicionario)


        self.software()

    def software(self):
        for i in range(6):
            frase = str(self.ouvir()).lower()

            if frase == None:
                frase = "."

            if "fechar" in frase:
                self.falar("Tudo bem, fico por aqui então! Até logo!")
                break

            if "aprender" in frase:
                self.aprender()

            if "pesquisar" or "pesquise" in frase:
                if "wikipédia" in frase:
                    self.wikipedia(frase)

                else:
                    self.navegador(frase)

                sleep(5)
                i=0

            if "iniciar" in frase:
                self.abrirSoftware(frase)
                sleep(5)
                i=0

            if "repetir" in frase:
                self.falar(texto= str(frase).replace("repetir ", ""), erro= "Desculpe, não conseigo repetir o que você disse, podemos tentar novamente?")
                i=0

            if i == 5:
                self.falar("Notei uma certa inatividade no sistema, irei encerrar por agora, okay? Até mais!")
                break

            i += 1

    def gravarUsuario(self):
        import config
        config()

        self.user_txt = open("./db/User.txt", "wt", encoding="utf-8")
        user = self.ouvir()
        print(self.user_txt.write(user))
        self.user_txt.close()

    def lerUsuario(self):
        self.user_txt = open("./db/User.txt", "rt", encoding="utf-8")
        self.user = self.user_txt.read()
        self.user_txt.close()

        return self.user

    def configurarMicrofone(self):
        self.voz = pyttsx3.init("sapi5")
        self.vozes = self.voz.getProperty("voices")
        x = 0

        for i in self.vozes:
            if "Saito" in str(i):
                break
            x += 1

        return self.vozes[x].id

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
            except:
                print(erro)

    def falar(self, texto, erro = "Desculpa, não consegui repetir essa frase, podemos tentar novamente?"):
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
            self.voz.setProperty("voice", self.microfone)
            self.voz.setProperty("volume", self.volume)
            self.voz.say(erro)
            self.voz.runAndWait()

    def abrirSoftware(self, comando):
        try:
            print(comando)
            os.startfile(str(comando).lower().replace("iniciar ","") + ".exe")
        except:
            self.falar("Não foi possível começar o software, tente novamente")

    def navegador(self, pagina):
        pesquisa = pagina.replace("pesquisar ","").replace("pesquise ","")
        wb.open(fr"www.google.com/search?q={pesquisa}".replace(" ","%20"))
        self.falar("Abrindo pesquisa na web")

    def wikipedia(self, comando):
        try:
            pesquisa = str(comando).replace("pesquisar na wikipédia ", "").replace("pesquise na wikipédia ", "")
            self.falar("Só um momento, estou procurando por " + pesquisa)
            wikipedia.set_lang("pt")
            resultado = wikipedia.summary(pesquisa,2)
            self.falar(texto= resultado, erro= "Não encontrei o resultado na Wikipedia.")
        except:
            self.falar("Não achei o resultado '{}' na wikipédia.".format(pesquisa))

    def tocarMusica(self, comando):
        musica = str(comando).replace("tocar ", "")
        pywhatkit.playonyt(musica)
        self.falar("Reproduzindo a música " + musica)

    def aprender(self):
        self.falar("Qual é a categoria?")
        categoria = self.ouvir()
        self.falar("Tudo bem, qual é o ítem que gostaria de aprender?")
        chave = self.ouvir()
        self.falar("Qual o valor que você quer atribuir a {}?".format(chave))
        try:
            significado = self.ouvir()
        except:
            self.falar("Desculpe, não entendi o que disse, poderia escrever para mim?")
            significado = input("Digite o local do arquivo, um link ou um significado: ")

        try:
            self.dados[categoria][chave] = significado
        except:
            self.dados[categoria] = {}
            self.dados[categoria][chave] = significado

        with open("db/Dicionário.json", "w", encoding="utf-8") as dicionario:
             json.dump(str(self.dados).lower().replace('"',''), dicionario, indent=2, ensure_ascii=False)
             self.falar("Entendi! Já armazenei essa informação!")


if __name__ == '__main__':
    Saito()