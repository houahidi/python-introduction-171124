# Afficher si chiffre pair ou impair
chiffre = input("Veuillez saisir un chiffre : ")
#conversion
chiffre = float(chiffre)
print("entier : ", int(chiffre))
reste = chiffre % 2
if reste == 0:
    print("Le nombre ", chiffre," est pair")
else :
    print("Le nombre ", chiffre," est impair")

if chiffre >= 0:
    print("Le nombre ", chiffre," est positif")
else :
    print("Le nombre ", chiffre," est negatif")
