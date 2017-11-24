

def moyenne(liste = []):
    somme = 0
    for elem in liste:
        somme = somme + elem
    resultat = somme / len(liste)
    #print("liste : ", liste , "moyenne :", resultat)
    return resultat

# le test est execute si le programme est le principal == __main__
# pas d'execution en cas d'import
if __name__ == "__main__":
    print("moyenne [1, 1, 1] = 1 == ", moyenne([1, 1, 1]))