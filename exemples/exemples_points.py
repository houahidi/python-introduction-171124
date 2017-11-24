
nombre = input("nombre points :")
nombre = int(nombre)
liste_points = []

for indice in range(1, nombre + 1):
    x = input("saisir x du point numero %s :" % indice)
    x = int(x)
    y = input("saisir y du point numero %s :" % indice)
    y = int(y)
    point = dict()
    point["x"]=x
    point["y"]=y
    # equivalente
    point = {"x" : x, "y" : y}
    liste_points.append(point)
for point in liste_points :
    print("Point(x:%d,y:%d)" % (point["x"],point["y"] ))
