# Afficher si chiffre pair ou impair
rang = input("Veuillez saisir le rang de la suite fibonacci:")
#conversion
rang = int(rang)
suite_fibo = [1, 1]

for indice in range(0, rang -2 + 1 , 1 ):
    new_elem = suite_fibo[-1] +suite_fibo[-2]
    suite_fibo.append(new_elem)
    print("fibo de ", indice + 2 ," = ", new_elem)
print("suite : ", suite_fibo)
