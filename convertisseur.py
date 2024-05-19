'''
Convertir des pouces (inch) en cm 

1 pouce = 2.54 cm 
1 cm = 0.394 pouces

 ex : un ecran de 17 pouces correspond à 43.18 cm (17*2.54cm)

 1) demander à l'utilisateur s'il souhaite convertir de pouces à cm ou de cm à pouces ? 
 2) demander à l'utilisateur de rentrer la valeur à convertir en précisant l'unité
 3) afficher la valeur  convertie (et l'unité : cm ou pouce)
 
 optionnel:
 Boucler pour convertir plusieurs valeurs (en conservant le sens de conversion), 
 et proposer une option pour sortir du programme
 '''

def effectuer_conversion (unit1: str, unit2: str, facteur: float ):
    valeur_str = input(f"conversion {unit1} en {unit2}. Donnez la valeur en {unit1} (ou 'q' pour sortir) : ")
    if valeur_str == "q" : 
        return True
    try :
        valeur_float = float(valeur_str)
    except ValueError:
        print ("Erreur ! Vous devez rentrer une valeur numérique !")
        print ("utilisez . et non , pour rentrer une valeur décimale.")
        return effectuer_conversion(unit1, unit2, facteur)

    valeur_convertie = round (valeur_float * facteur, 2)
    print (f'Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}')
    return False

while True :
    print("Bienvenue dans mon programme de conversion d'unités.")
    print("Ici vous pourrez convertir des pouces en cm et vice et versa !")
    print("Tapez 1 pour convertir des pouces en cm")
    print("Tapez 2 pour convertir des cm en pouces")

    reponse = input("Faite votre choix (tapez 1 ou 2) : ")
    if reponse = "1" or "2":
        break
    print("Erreur : Vous devez choisir 1 ou 2 ! \n")

while True:
    if  reponse == "1":
        if effectuer_conversion ('pouces', 'cm', 2.54):
            break

    if reponse == "2": 
        if effectuer_conversion ('cm', 'pouces', 0.394):
            break 
