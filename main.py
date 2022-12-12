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

                #Verifica se a frase está vazia.
            if frase == None:
                frase = "."

                #Encerra o software.
            if "fechar" in frase:
                self.falar("Tudo bem, fico por aqui então! Até logo!")
                break

                #Aumenta/Diminui o volume
            if "volume" in frase:
                self.controleVolume(frase)
                i=0

                #Lhe mostra uma lista com todos os comandos do Software
            if "comando" in frase:
                self.comandos()
                sleep (10)
                i=0


                #Pesquisa no Google/Wikipédia a frase dita pelo usuário.
            if "pesquisar" in frase or "pesquise" in frase:
                if "wikipédia" in frase:
                    self.wikipedia(frase)
                else:
                    self.navegador(frase)
                    
                sleep(5)
                i=0

                #Inicia um software com base no que estiver guardado no Dicionário.json
            if "iniciar" in frase:
                self.abrirSoftware(frase)
                sleep(5)
                i=0

                #Repete a frase que o usuário falar.
            if "repetir" in frase:
                self.falar(texto= str(frase).replace("repetir ", ""), erro="Desculpe, não conseigo repetir o que você disse, podemos tentar novamente?")
                i=0

                #Pesquisa uma música no YouTube e abre a página para você.
            if "música" in frase:
                self.tocarMusica(frase)
                sleep(3)
                i=0

                #Pesquisa um CNPJ utilizando a API da Receita WS
            if "cnpj" in frase:
                self.verificarCNPJ()
                sleep(3)
                i=0

                #Verifica um total de 10x se existe interação ao sistema, e caso não aja interação o sistema desliga sozinho.
            if i == 10:
                self.falar("Notei uma certa inatividade no sistema, irei encerrar por agora, okay? Até mais!")
                break


if __name__ == '__main__':
    Saito()
