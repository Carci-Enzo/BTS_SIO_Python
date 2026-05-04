"""#exercice 1 
def majorite(age):
    if age < 18:
        print("mineur")
    else:
        print("majeur")
majorite(18)
#exercice 2 
def majorite(age):
    if age < 12 : 
        print("enfant")
    elif age <= 17 :
        print ("adolescent")
    elif age <= 64 : 
        print("adulte")
    else :
        print( "sénior")
majorite(65)
#exercice 3 
def calculateur(nombre1,nombre2,operateur):
    if operateur == "addition" : 
        print( nombre1 + nombre2 )
    elif operateur == "multiplication" :
        print ( nombre1 * nombre2 )
    elif operateur == "division":
        print ( nombre1 / nombre2)
    elif operateur == "soustraction":
        print (nombre1 - nombre2) 
    else : 
        print ( " choisit additions, soustraction, multiplication ou division " )
calculateur( 4, 5, "multiplication")
#exercice4"""
def connexion(login,mdp):
    if login != "root" and mdp != "!!_Ca_C_pYthon_**":
        print ( "Identifiant incorrect ou Mot de passe incorrect")
    elif login == "root" and mdp != "!!_Ca_C_pYthon_**":
        print("Identifiant incorrect ou Mot de passe incorrect")
    elif login != "root" and mdp == "!!_Ca_C_pYthon_**":
        print("Identifiant incorrect ou Mot de passe incorrect")
    else : 
        print("Connexion réussie")
connexion("gdfgdfg", "!!_Ca_C_pYthon_**")