# Afficher si chiffre pair
saisie = input("Veuillez saisir un chiffre : ")
#conversion
chiffre = float(saisie)
#Afficher les chiffres positifs pairs <= chiffre
nombre = 0
indice = 1
while nombre <= chiffre:
    print("nombre pair ", indice,"= ", nombre)
    nombre = nombre + 2  # nombre += 2
    indice = indice + 1  # indice += 1
# solution avec for
indice =0
for elem_pair in range(0, int(chiffre) + 1, 2):
    print("nombre pair ", indice, "= ", elem_pair)
    indice = indice + 1 # indice += 1