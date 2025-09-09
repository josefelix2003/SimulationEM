#------------TP1-----------------

#Exo1
def table_mult(a, b):
    #a : numero de la table
    #b : ordre de la table 
    for n in range (1,b+1):
        print(f"{n}*{a} = {n*a}")
        
#Exo2
def table_conversion(valeur_conv):
    #valeur_conv : valeur conversion euro-dollar
    n=1
    while n<=16384:
        print("{} euro(s) = {} dollar(s)".format(n, n*valeur_conv))
        n*=2
        
#Exo3
def suite_triple(n):
    triples_list=[n]
    for i in range(11):
        triples_list.append(triples_list[i]*3)
    print(triples_list)
    
#Exo4
def compute_volume(width, heigth, depth):
    return width*heigth*depth

#Exo5
def conv_secondes(sec):
    n_days=sec//86400
    res=sec%86400
    n_hours=res//3600
    res=res%3600
    n_min=res//60
    n_sec=res%60
    print(f"{sec} secondes = {n_days} jours {n_hours} heures {n_min} minutes {n_sec} secondes")
    
#Exo6
    def table_mult_astersique(a, b, c):
        #a : numero de la table
        #b : ordre de la table 
        #c : multiple  vérifier
        for n in range (1,b+1):
            if n*a%c == 0:
                print(f"{n}*{a} = {n*a} *")
            else:
                print(f"{n}*{a} = {n*a}")
                
#Exo7
def affichage_pyramide(n1, n2):
    #n1 : premier numero de la pyramide
    #n2 : dernier numero de la pyramide
    c=n1
    while c<=n2:
        for i in range (c):
            print(i+1, end=" ")
        print("\n")
        c+=1
        
#Exo8
def affichage_pyramide_inv(n1, n2):
    #n1 : premier numero de la pyramide
    #n2 : dernier numero de la pyramide
    c=n2
    while c>=n1:
        for i in range (c):
            print(i+1, end=" ")
        print("\n")
        c-=1
        
    
