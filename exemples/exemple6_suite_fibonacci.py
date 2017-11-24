# Afficher si chiffre pair ou impair
rang = input("Veuillez saisir le rang de la suite fibonacci:")
#conversion
rang = int(rang)
U0 = 1
U1 = 1

for indice in range(0, rang -2 + 1 , 1 ):
    Un = U0 + U1
    U0 = U1
    U1 = Un
    print("fibo de ", indice + 2 ," = ", Un)

