class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def affiche(self):
        print(f"voiture {self.marque} {self.modele}")
class Parc:
    def __init__(self,id,adresse,capacite):
        self.id =id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []