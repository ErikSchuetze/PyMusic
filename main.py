import os
import random
import inquirer
import threading
from playsound import playsound

class RandomMusics:
    pasta = "./random music/Music"
    arquivos = []
    arquivos = os.listdir(pasta)
    quantidade = len(arquivos)
    programa = True
    n = "Ainda nada"
    
    def musgasAleatoria(self):
        self.n = random.choice(self.arquivos)
        play = self.n.find(".")
        if self.n[play:] == ".mp3":
            pass
        else:
            self.musgasAleatoria()
            
    def status(self):
        print(f"""
Musica no momento: "{self.n}"
Para parar aperte CTRL + C
_____________________________
        """
        )
        
    def activity_voltar(self):
        self.n = self.m
        
    def activity_pular(self):
        self.m = self.n
        self.musgasAleatoria()
        self.activity_comecar()
        

    def activity_pausar(self):
        print("Desculpe, eu ainda não achei como pausar musica com o playsound python")

    def activity_parar(self):
        self.programa = False
       
    def activity_comecar(self):
        self.musgasAleatoria()
        playsound(f"./random music/Music/{self.n}")
        

    def run(self):
        self.clear()
        self.status()
        question = [
            inquirer.List(
                "activity",
                choices=["Voltar", "Pausar", "Comecar", "Parar", "Pular",],
            ),
        ]
        answer = inquirer.prompt(question)
        activity_name = "activity_{}".format(answer.get("activity")).lower()
        activity = threading.Thread(target=getattr(self, activity_name, lambda: "Invalid activity"))
        (status) = activity.start()
        print(status)
    
    def clear(self):
        sys = os.name
        if sys =="nt":
           _ = os.system('cls')
        else:
           _ = os.system('clear')


def main():
    tamago = RandomMusics()
    
    t = threading.Thread(target=tamago.activity_comecar)
    t.start()
    tamago.run()

    while tamago.programa:
        tamago.run()
    
if __name__ == "__main__":
   main()
