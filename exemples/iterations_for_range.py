
# creer une liste en utilisant range
formule1 = range(0, 11, 2) # generateur de liste
liste1 = list(formule1)
print("formule1 : ", formule1)
print("liste1   : ", liste1)

# afficher les elements de la liste avec for
for elem in liste1:
    print("elem :",elem)
#equivalent
for elem in formule1:
    print("elem avec formule1 :", elem)