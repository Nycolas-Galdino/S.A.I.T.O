from time import sleep
import actions

actions = actions.actionsSaito

class Saito(actions):
    def __init__(self):
        super(Saito, self).__init__()
        self.software()

    def software(self):
        for i in range(11):
            frase = str(self.ouvir()).lower()

            if frase == None:
                frase = "."

            if "fechar" in frase:
                self.falar("Tudo bem, fico por aqui então! Até logo!")
                break

            if "volume" in frase:
                self.controleVolume(frase)
                i=0

            if "aprender" in frase:
                self.aprender()
                i=0

            if "pesquisar" in frase or "pesquise" in frase:
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
                self.falar(texto= str(frase).replace("repetir ", ""), erro="Desculpe, não conseigo repetir o que você disse, podemos tentar novamente?")
                i=0

            if "música" in frase:
                self.tocarMusica(frase)
                sleep(3)
                i=0

            if i == 10:
                self.falar("Notei uma certa inatividade no sistema, irei encerrar por agora, okay? Até mais!")
                break


if __name__ == '__main__':
    Saito()
