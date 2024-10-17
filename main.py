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

    def musgasAleatoria(self, arquivos):
        self.n, self.m = random.choice(arquivos)
        
    def status(self):
        print(f"""
Musica no momento: "{self.n}"
Para parar aperte CTRL + C
""")
        
    def activity_voltar(self):
        self.n = self.m
        
    def activity_pular(self, arquivos):
        self.m = self.n
        self.n = random.choice(arquivos)

    def activity_pausar(self):
        print("Desculpe, eu ainda não achei como pausar musica com o playsound python")

    def activity_comecar(self):
        print("Por eu não entender como faz para pausar, essa e a função de pausar estão inativas")

    def activity_parar(self):
        self.programa = False


    def run():
        question = [
            inquirer.List(
                "activity",
                message="O quer fazer?",
                choices=["Voltar", "Pausar", "Comecar", "Parar", "Pular",],
            ),
        ]
        answer = inquirer.prompt(question)
        activity_name = "activity_{}".format(answer.get("activity")).lower()
        activity = getattr(activity_name, lambda: "Invalid activity")
        (status, sleep) = activity()
        print(status)
    
    def começar(self):
        playsound(f"./random music/Music/{self.n}")

def main():
    tamago = RandomMusics
    
    t = threading.Thread(target=tamago.run())
    
    while tamago.programa:
        t.start()
    tamago.activity_comecar()
    
if __name__ == "__main__":
    main()