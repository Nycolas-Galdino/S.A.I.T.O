import json
import os
import pyttsx3
import pywhatkit
import requests
import speech_recognition as srLib
import webbrowser as wb
import wikipedia
from ast import literal_eval


class actionsSaito:

    def __init__(self):
        self.nome = "Saito Shion Cipriano"
        self.microfone = None
        self.volume = 0.5

        if self.lerUsuario() == "":
            self.gravarUsuario()

        self.usuario = self.lerUsuario()

        self.falar(f"Olá {self.user}, como posso lhe ajudar? \n")

        print("Caso queira ver os comandos, é só falar 'comandos' e aparecerá uma lista de comandos.")

        try:
            with open("Dicionário.json", "r", encoding="utf-8") as dicionario:
                self.dados = literal_eval(json.load(dicionario))

        except: pass

    def gravarUsuario(self):
        import config
        config

        self.user_txt = open(os.getcwd() + "/User.txt", "wt", encoding="utf-8")
        user = self.ouvir(erro="")
        while user == None:
            self.falar("Desculpa, não entendi seu nome, poderia repetir?")
            user = self.ouvir(erro="")
        print(self.user_txt.write(user))
        self.user_txt.close()

    def lerUsuario(self):
        self.user_txt = open(os.getcwd() + "/User.txt", "rt", encoding="utf-8")
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

    def ouvir(self, frase="*Ouvindo*", erro="Desculpa, não entendi direito."):
        mic = srLib.Recognizer()

        try:
            with srLib.Microphone() as gravacao:
                mic.adjust_for_ambient_noise(gravacao, duration=2, )
                print(frase)
                audio = mic.listen(gravacao, phrase_time_limit=10)
            texto = mic.recognize_google(audio, language="pt-BR")
            print(f"Você disse: '{texto}'")
            return texto
        except:
            print(erro)

    def falar(self, texto, erro="Desculpa, não consegui repetir essa frase, podemos tentar novamente?"):
        print(texto)
        try:
            if self.microfone is None:
                self.microfone = self.configurarMicrofone()

                # Velocidade do som

            self.voz.setProperty("voice", self.microfone)
            self.voz.setProperty("volume", self.volume)
            self.voz.say(texto)
            self.voz.runAndWait()
        except:
            self.voz.setProperty("voice", self.microfone)
            self.voz.setProperty("volume", self.volume)
            self.voz.say(erro)
            self.voz.runAndWait()

    def abrirSoftware(self, comando):   #Falta implementar no main.py
        try:
            print(comando)
            os.startfile(str(comando).lower().replace("iniciar ", "") + ".exe")
        except:
            self.falar("Não foi possível começar o software, tente novamente")

    def navegador(self, pagina):
        pesquisa = pagina.replace("pesquisar ", "").replace("pesquise ", "")
        wb.open(fr"www.google.com/search?q={pesquisa}".replace(" ", "%20"))
        self.falar("Abrindo pesquisa na web")

    def wikipedia(self, comando):
        try:
            pesquisa = str(comando).replace("pesquisar", "")
            pesquisa = str(comando).replace("pesquise", "")
            pesquisa = str(pesquisa).replace("wikipédia ", "")
            pesquisa = str(pesquisa).replace("na", "")
            pesquisa.strip()

            self.falar("Só um momento, estou procurando por " + pesquisa)
            wikipedia.set_lang("pt")
            resultado = wikipedia.summary(pesquisa, 2)
            self.falar(texto=resultado, erro="Não encontrei o resultado na Wikipedia.")
        except:
            self.falar("Não achei o resultado '{}' na wikipédia.".format(pesquisa))

    def tocarMusica(self, comando): 
        musica = str(comando).replace("tocar música ", "")
        pywhatkit.playonyt(musica)
        self.falar("Reproduzindo a música " + musica)

    def perguntas(self):
        pass
    
    def senhas(self):
        with open(os.getcwd() +"/senhas.json", "w", encoding="utf-8") as senhas:
            senhas = print(literal_eval(json.load(senhas)))

    def verificarCNPJ(self):
        self.falar("Por favor, digite o CNPJ desejado utilizando apenas números")
        cnpj = input("CNPJ => ")         
        
        try:
            response = requests.get(url=f"https://receitaws.com.br/v1/cnpj/{int(cnpj)}")

            response_json = response.json()

            self.falar(fr"""A razão social é {response_json['nome']} e o nome fantasia é {response_json['fantasia']}, caso queira mais informações, seguem descritas abaixo.""")
            print(response_json['ultima_atualizacao'])
            print(f"CEP: {response_json['cep']}")
            print(f"Endereço completo: {response_json['logradouro']}, {response_json['municipio']}, {str(response_json['uf']).upper()} - {response_json['numero']} \n Complemento: {response_json['complemento']}"
                  )
        except:
            self.falar("Desculpe, não consegui encontrar o CNPJ desejado.")

    def controleVolume(self, comando):
        if len(comando) <= 50:
            self.voz.setProperty("rate", 200)
        elif len(comando) <= 100:
            self.voz.setProperty("rate", 250)
        elif len(comando) <= 200:
            self.voz.setProperty("rate", 300)
        else:
            self.voz.setProperty("rate", 350)

            # Volume
        if self.volume == 1 and comando == "aumentar o volume":
            return self.falar("O volume está no máximo")

        if self.volume == 0.25 and comando == "diminuir o volume":
            return self.falar("O volume está no mínimo")

        if comando == "aumentar o volume" and self.volume < 1:
            self.volume += 0.25
            return self.falar("O volume está em {}%".format(100 * (self.volume / 1)))

        if comando == "diminuir o volume" and self.volume > 0.25:
            self.volume -= 0.25
            return self.falar("O volume está em {}%".format(100 * (self.volume / 1)))

    def comandos(self):
        listaDeComandos = """COMANDOS:
        
        Abrir planilhas;
            #Em Desenvolvimento
            
        Abrir Softwares;
            #Em desenvolvimento;
                        
        Ouvir Músicas;
            Diga "Tocar música" e o nome da música;
           
        Pesquisar na Web;
            Diga "Pesquisar" ou "Pesquise" e o resultado que deseja pesquisar.
            
        Pesquisa na Wikipedia;
            Diga "Pesquisar na wikipédia" ou "Psquise na wikipédia" e o resultado que desejar.
                
        Repetir Frase;
            Diga "Repetir" e a frase que deseja.
            
        Pesquisar CNPJ
            Diga "Pesquisar por CNPJ", isso irá lhe retornar alguns dados do CNPJ desejado.
            
        """

        print(listaDeComandos)
        self.falar("Esses são meus comandos, posso lhe ajudar em algo mais?")