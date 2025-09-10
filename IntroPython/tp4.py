#TP POO partie 1

#Création d'une classe voiture
class Point:
    "Definition d'un point geometrique"

a = Point()
a.x = 1
a.y = 2
b = Point()
b.x = 3
b.y = 4
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)

class Voiture:
    "Classe Voiture"
    def __init__(self):
        self.marque=""
        self.modele=""
        self.annee=0
        self.kilometrage=0
        
v=Voiture()




