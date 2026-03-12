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

    def entrerVoiture(self, voiture):
        if len(self.listeVoitures) >= self.capacite:
            print("parc plein")
            return
        self.listeVoitures.append(voiture)
        print("voiture entrée")

    def sortirVoiture(self, voiture):
        if voiture in self.listeVoitures:
            self.listeVoitures.remove(voiture)
            print("voiture sortie")
        else:
            print("voiture non trouvée")

    def calculuerNbrPlacesLibres(self):
        return self.capacite - len(self.listeVoitures)
parc1 = Parc(1, "Montreal",2)
v1 = Voiture("Toyota" , "Corolla")
parc1.entrerVoiture(v1)
parc1.sortirVoiture(v1)
