chiffre = input('Vas y!! A toi de jouer! Saisis une suite de chiffres : ')
#conversion

factoriel = int(chiffre)
affichage = "" + str(chiffre)
for elem in range(int(chiffre) -1, 1, -1):
    affichage += "*" + str(elem)
    factoriel = factoriel * elem
    #print ("A ce stade le factoriel est ", factoriel,".")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("La factoriel de ", chiffre,":", affichage,"=",factoriel,".")