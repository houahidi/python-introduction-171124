chiffre = input('Vas y!! A toi de jouer! Saisis chiffre: ')

liste =[1,1]

for elem in range(int(chiffre)-1):
    new_val = int(liste[-1]) + int(liste[-2])
    liste.append(new_val)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("Au rang", chiffre," la valeur de la liste de Fibonacci est ",liste[-1])