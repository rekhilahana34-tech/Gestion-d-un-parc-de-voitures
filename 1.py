class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def affiche(self):
        print(f"voiture {self.marque} {self.modele}")