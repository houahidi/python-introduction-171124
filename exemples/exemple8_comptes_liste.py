

compte1 = [1, 100]
compte2 = [2, 1000000]
compte3 = [3, -110]
comptes = [compte1, compte2, compte3]


numero = int(input("numero de compte :"))
somme = float(input("somme a crediter :"))
for compte in comptes:
    if compte[0] == numero:
        print("numero ", compte[0], " ,solde:", compte[1])
        compte[1] += somme
        print("numero ", compte[0], " ,solde:", compte[1])

somme = float(input("somme a debiter :"))
numero = int(input("numero de compte :"))
for compte in comptes:
    if compte[0] == numero:
        print("numero ", compte[0], " ,solde:", compte[1])
        compte[1] -= somme
        print("numero ", compte[0], " ,solde:", compte[1])
