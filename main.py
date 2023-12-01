#initialisation de la liste
historique=[]
#creation de la fonction qui va permettre de faire le calcul
def calculatrice(num1,operateur,num2):
    try:
#bloc de condition qui reconnait l'operateur choisit par l'utilisateur et qui retourne le resultat des deux nombre rentrés
        if operateur == "+":
            return num1 + num2
        elif operateur == "-":
            return num1 - num2
        elif operateur == "*":
            return num1 * num2
        elif operateur == "/":
            if num1 and num2 == 0:
                return "division par zero impossible"
            else:
                return num1 / num2  
        else:
            return "Opérateur inconnu"
    except ValueError:
        print(f"erreur")   
#fin de la fonction
# creation d'une boucle qui nous demande les operations            
while True:
    var1=float(input("1er nombre : "))
    var2=input("operation : ")
    var3=float(input("2eme nombre : "))

#après avoir rentré l'opération , on utilise la fonction pour calculer
    print(f"{var1} {var2} {var3} = {calculatrice(var1,var2,var3)}")

#on ajoute le resultat dans la liste historique
    historique.append(f"{var1} {var2} {var3} = {calculatrice(var1,var2,var3)}")

#on demande a l'utilisateur si il veut l'historique. Si il ne le veut pas le tour de la boucle fini ici pour redemander une opération
    reponse=input("tapez 1 pour avoir l'historique , tapez 2 pour ne pas l'avoir : ")
    if reponse== "1":
        print("HISTORIQUE :")
        #ça va print chaque élément(opérations) de la liste historique
        for i in historique:
            print(i)        
        #ça va demander a l'utilisateur si il veut effacer l'historique.Si il ne le veut pas le tour de la boucle fini ici pour redemander une opération
        rep=input("voulez-vous effacer l'historique ?(1=oui/2=non) :")     
        if rep=="1":
            for i in range(len(historique)):#cette boucle va effacer chaque éléments de la liste historique.
                del(historique[0])   
#fin du tour de la boucle
                     
