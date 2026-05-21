"""
#exercice1
def compteur_simple():
    i = 1
    while i <= 10 :
        print(i)
        i = i + 1 
compteur_simple()
#exercice2
def compteur_a_rebours():
    i = 10
    while i >= 1 :
        print(i)
        i = i - 1
compteur_a_rebours()
#exercice3
def somme_de_nombres():
    nombre_n= int(input("veuillez écrire votre nombre s'il vous plaît : "))
    somme_de_nombres_n = 0
    i = 1
    while  i <= nombre_n :
        somme_de_nombres_n = i + somme_de_nombres_n
        i = i + 1
    print(somme_de_nombres_n)
somme_de_nombres()         


            
#exercice4maisrevenirsurletroisaprès
"""
def mot_de_passe ():
    mot_de_passe_1 = "BozuKatodic"
    tentative_user = str(input( "Entrez votre mot de passe : "))
    i =  0
    while i < 4 : 
         if tentative_user != mot_de_passe_1 :
            tentative_user = str(input( "Recommance petite pute : "))
         else:
             print("accès autorisé")
             return
         i = i + 1
    print( "Trop de tentative" )
    
mot_de_passe()
