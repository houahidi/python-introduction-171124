
# utilisation des dictionnaires : couple cle, valeur
compte1 = dict()
compte1["numero"] = 1
compte1["solde"] = 100
#equivalente a
compte1 = {"numero": 1, "solde" : 100}
#creer d'autres comptes
compte2 = {"numero": 2, "solde" : 1000000}
compte3 = {"numero": 3, "solde" : -110}
#creer une liste de comptes
comptes = [compte1, compte2, compte3]

#operation sur les comptes
numero = int(input("numero de compte :"))
somme = float(input("somme a crediter :"))
for compte in comptes:
    if compte["numero"] == numero:
        print("numero ", compte["numero"], " ,solde:", compte["solde"])
        compte["solde"] += somme
        print("numero ", compte["numero"], " ,solde:", compte["solde"])

somme = float(input("somme a debiter :"))
numero = int(input("numero de compte :"))
for compte in comptes:
    if compte["numero"] == numero:
        print("numero ", compte["numero"], " ,solde:", compte["solde"])
        compte["solde"] -= somme
        print("numero ", compte["numero"], " ,solde:", compte["solde"])
