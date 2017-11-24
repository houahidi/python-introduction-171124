# valeur par defaut d'un parametre
def fibonacci(rang=3):
    # Afficher si chiffre pair ou impair
    U0 = 1
    U1 = 1

    for indice in range(0, rang -2 + 1 , 1 ):
        Un = U0 + U1
        U0 = U1
        U1 = Un
    print("fibo de ", indice + 2 ," = ", Un)

#fibo d'un rang demande a l'utilisateur
rang = input("Veuillez saisir le rang de la suite fibonacci:")
#conversion
rang = int(rang)
fibonacci(rang)
#fibo de 6
print("fibonacci de 6")
fibonacci(6)
fibonacci()

