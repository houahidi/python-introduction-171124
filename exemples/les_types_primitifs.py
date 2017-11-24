
print("Manipulation des types primitifs")
print("Cas I : boolean : True, False")
variableBool = True
variableBool = bool(True)
print("VariableBool = ", variableBool)
print("inverse VariableBool = ", not variableBool)
print("variableBool and True : ",  variableBool and True)
print("variableBool and False : ",  variableBool and False)
print("variableBool or True : ",  variableBool or True)
print("variableBool or False : ",  variableBool or False)
print("bool(0)=", bool(0))
print("bool(1)=", bool(1))
expression = bool(None)
print("bool(None)=", expression)  # None = null : n'est pas definit

print("Cas II : entier :  -2puissance((8*4)-1), 2puissance((8*4)-1)-1")
entier = 12
entier = int(12)
print("entier : ", entier, ", type :", type(entier))
print("addition     : 5 + 2 =  ", 5 + 2)
print("soustraction : 5 - 2 =  ", 5 - 2)
print("division     : 5 / 2 =  ", 5 / 2)
print("multiplication:5 * 2 =  ", 5 * 2)
print("modulo       : 5 % 2 =  ", 5 % 2)  #reste de la division entiere

print("Cas III : reel :  1.79e308")
reel = 12.0
reel = float(12)
print("reel : ", reel, ", type :", type(reel))
print("addition     : 5 + 2.0 =  ", 5 + 2.0)
print("soustraction : 5 - 2.0 =  ", 5 - 2.0)
print("division     : 5 / 2.0 =  ", 5 / 2.0)
print("multiplication:5 * 2.0 =  ", 5 * 2.0)

print("Cas IV : chaine de caractere :  suite de caracteres non modifiable")
chaine ="ma chaine de caracteres"
chaine =str("ma chaine de caracteres")
print("chaine = ", chaine, ", type :", type(chaine))
expresion = 'bonjour' + ' ' + "Pascal"
print("concatenation : 'bonjour' + \"Pascal\" :",expresion)
print("1er caractere     : ", chaine[0])
print("dernier caractere : ", chaine[-1])
print("nombre de carcteres:", len(chaine))
print("sous chaine :", chaine[3:9])
print("les 2 derniers caracters :", chaine[-2:])
print("les 2 premiers caracters :", chaine[:2])
# chaine[3] = 'C' : impossible de modifier la chaine