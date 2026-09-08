class Game:
    def __init__(self, enigmes):
        self.enigmes = enigmes
        self.door = Door()
        self.current_enigme_index = 0

    def start(self):
        while self.current_enigme_index < len(self.enigmes):
            current_enigme = self.enigmes[self.current_enigme_index]
            print(f"Énigme {self.current_enigme_index + 1}:")
            if current_enigme.poser_question():
                print("Bonne réponse !")
                self.current_enigme_index += 1
            else:
                print("Mauvaise réponse. Essayez encore.")
                current_enigme.donner_indice()
        print("Félicitations ! Vous avez résolu toutes les énigmes.")
        self.door.unlock()

class Enigme:
    def __init__(self, question, reponse, indice, lettre = None):
        self.question = question
        self.reponse = reponse
        self.indice = indice
        self.lettre = lettre
        self.solved = False

    def poser_question(self):
        print(self.question)
        user_reponse = input("Votre réponse: ")
        return self.check_reponse(user_reponse)

    def check_reponse(self, user_reponse):
        if user_reponse.lower() == self.reponse.lower():
            self.solved = True
            return True
        else:
            return False
    
    def donner_indice(self):
        print("Indice: " + self.indice)

    def get_lettre(self):
        return self.lettre

class Door(Enigme):
    def __init__(self, question, reponse, indice, indice2):
        super().__init__(question, reponse, indice)
        self.indice2 = indice2
        self.locked = True

    def donner_indice2(self):
            print("Indice: " + self.indice2)

    def unlock(self):
        if self.solved:
            self.locked = False
            print("La porte est maintenant déverrouillée.")
        else:
            print("Vous devez résoudre l'énigme pour déverrouiller la porte 2.")