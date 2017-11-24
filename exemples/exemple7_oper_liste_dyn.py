# Afficher si chiffre pair ou impair
taille = input("Veuillez saisir la taille :")
#conversion
taille = int(taille)
# liste d'elements vide
elements = []
for indice in range(1, taille+1):
    message ="Veuillez saisir element " +str(indice) + ":"
    new_elem = input(message)
    #conversion
    new_elem = float(new_elem)
    elements.append(new_elem)
#Fin de recuperation des elements
elements.sort()
print("min : ", elements[0])
print("max : ", elements[-1])
#calcule de la somme
somme = 0
for elem in elements:
    somme = somme + elem
print("somme : ", somme)
#calcul moyenne
print("moyenne :", somme/taille)