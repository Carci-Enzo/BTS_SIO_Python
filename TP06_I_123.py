#exercice 1
""""
def age_verification():
    age = int(input("Quel est votre âge ? Ton âge est : "))
    if age >= 18 :
        print("Vous êtes majeur, vous pouvez tuer votre foie ! ")
    else :
        print("Tu es mineur, que du jus pour toi... Mais on dit aussi 'pas vue pas pris' °^ ")
age_verification()

#exercice 2
def type_de_nombres() : 
    nombre = int(input("Ecris ton nombres : "))
    if nombre > 0 :
        print("Ton nombres est positif ")
    elif nombre == 0 :
        print("Ton nombres est égal à zéros ")
    else :
        print("Ton nombres est négatif ")
type_de_nombres() 
"""
#exercice 3 
def verification_de_mot_de_passe(): 
    mot_de_passe = "pYth0n123*%?"
    tentative = str(input( "Veuillez-saisir votre mot de passe : ")) # pyright: ignore[reportInvalidTypeForm]
    validation = tentative == mot_de_passe
    if validation :
        print("Accès autorisée ! ")
    else :
        print("Mot de passe incorecte veuillez réessayer ") 
verification_de_mot_de_passe()
