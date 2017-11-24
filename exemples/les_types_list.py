# Cas I : liste modifiable
#initialisation
liste1 = []    # liste vide
liste1 = list() # liste vide
liste1 = ["chaine", 2, 5.0, True] #une liste d'objets
#acces aux elements
print("liste : ", liste1)
print("1er element : liste[0] :", liste1[0])
print("dernier element : liste[-1] :", liste1[-1])
# les listes sont des objets sur lequelles  on peut appliquer
# des actions (methodes)
# help(liste) => affiche les # actions
liste1.append("ajout a la fin")
print("liste : ", liste1)
# elle retourne le dernier element supprime
dernier = liste1.pop(-1)
print("liste : ", liste1, "dernier :", dernier)
#nombre d'occurences d'un element
print("nombre d'occurences de l'element 2 : ", liste1.count(2))
print("Taille de la liste : ", len(liste1))
#ajouter les elements d'une liste
autreliste = [1, 2]
liste1.extend(autreliste)
print("liste : ", liste1)
print("Taille de la liste : ", len(liste1))
# creer une copie d'une liste
copie_liste = liste1[:]
copie_liste = liste1.copy()
copie_liste.append("element dans la copie")
print("copie_liste : ", copie_liste)
print("liste : ", liste1)
# creer une nouvelle variable qui reference la meme liste
tableau1 = liste1
liste1.append("elem")
print("liste1 : ", liste1)
print("tableau1 : ", tableau1)

# Cas II : liste non modifiable
tuple1 = tuple(liste1)
print("tuple1", tuple1, "type :", type(tuple1))
print("taille : ", len(tuple1))
print("1er element : ", tuple1[0])
tuple_copie = tuple1[:]
print("tuple1", tuple1)
print("tuple_copie", tuple_copie)