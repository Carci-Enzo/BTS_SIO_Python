
def mot_de_passe():
    i = 0 
    password = "EnmOde5ha77a"
    tentative_user = str(input(" Veuillez entrer votre mot de passe : ")) 
    while i < 2 :
         if tentative_user != password : 
            i = i+1
            tentative_user = str(input(" Recommancez s'il vous plaît : "))
         else :
             print("mot de passe correcte")
             return

    print( "Trop de tentatives bougé ! ")
mot_de_passe()