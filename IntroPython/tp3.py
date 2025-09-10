#TP Valeurs/Vecteurs Propres
import numpy as np
from numpy.linalg import eig

sigma_y = np.array([[0, -1j],
                    [1j, 0]])

#Vérification matrice hermitique
sigma_y_trans_comp = np.conj(sigma_y).T

if np.array_equal(sigma_y, sigma_y_trans_comp):
    print("La matrice sigma_y est bien hermitique")
else:
    print("La matrice sigma_y n'est pas hermitique")
    
#Calcul valeurs/vecteurs propres
D, V = eig(sigma_y)

val1=D[0]
val2=D[1]
print("Valeurs propres : ")
for i in D:
    print(i)


vect1=V[:,0]
vect2=V[:,1:2]  
vect1.shape=(2, 1)  
vect2.shape=(2, 1)  
print("\nVecteurs propres : \nVecteur 1 :")
print(vect1,"\nVecteur 2 :\n",  vect2)
    
#Vérifier rélation d'orthogonalité
np.dot(np.conj(vect2).T, vect1)
np.isclose(np.dot(np.conj(vect2).T, vect1), 0).all()
np.allclose(np.dot(np.conj(vect2).T, vect1), 0)

#Projecteurs
P1=np.dot(vect1, np.conj(vect1).T)
P2=np.dot(vect2, np.conj(vect2).T)

#Vérification rélation de fermeture 
I=P1+P2

#Produit P1P2, P2P1
p1p2=np.dot(P1, P2)
p2p1=np.dot(P2, P1)


    


