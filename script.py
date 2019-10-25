from dictionnaire import villes
from math import *
from time import *

def livraison(depart, arrivee):
    vitesse_m = 0
    distance_trajet = villes[depart][arrivee] * 1000
    distance_parcourue = 0
    temps_s = 0
    t_avant_pause = 0
    pause = False
    nb_Pause = 0
    distance_restante = 0
    while (distance_parcourue < distance_trajet):

        if (t_avant_pause == 6660):
            pause = True
            

        if (pause == True):
            if (vitesse_m > 25/9):
                vitesse_m -= 25 / 9
                temps_s += 60
                distance_parcourue += vitesse_m * 60
            elif (vitesse_m < 25/9):
                temps_s += 900
                t_avant_pause = 0
                vitesse_m = 0
                pause = False
                nb_Pause += 1
        else:
            temps_s += 60
            t_avant_pause += 60
            distance_parcourue += vitesse_m * 60

        if (t_avant_pause < 600):
            if (vitesse_m < 25):
                vitesse_m += 25 / 9
                distance_parcourue += vitesse_m * 60

        distance_restante = (distance_trajet - distance_parcourue)
        while ( distance_restante <= 6500 ):
            t_avant_pause += 20000
            distance_restante = (distance_trajet - distance_parcourue)
            if (vitesse_m > 25 / 9):
                vitesse_m -= 25 / 9
                temps_s += 60
                distance_parcourue += vitesse_m * 60
            elif (vitesse_m < 25/9):
                vitesse_m = 0
                return int(distance_parcourue), temps_s
        
        
        

    
    


def multipleVille():
    villes_demande = None
    entry_villes = []
    temps_total = 0
    distance_total = 0

    while villes_demande != "" or len(entry_villes) < 2:
        villes_demande = input("\nVeuillez fournir autant de ville que vous le souhaitez, lorsque vous avez fini, veuillez faire entrée: \n").lower().title()
        if villes_demande.isalpha():
            if villes_demande in villes:
                entry_villes.append(villes_demande)
            else:
                print("\nVeuillez demander une ville présente dans notre base de données, situé dans le fichier dictionnaire.py \n")
        elif villes_demande.isalpha() == False and villes_demande != "":
            print("\nVeuillez fournir uniquement des lettres lors de votre sélection, merci \n")
            
        if len(entry_villes) < 2 and villes_demande == "":
            print("\nVous devez me fournir, au moins 2 villes, merci.\n")

    for i in range(len(entry_villes)-1):
        distance_parcourue,temps_s = livraison(entry_villes[i], entry_villes[i+1])
        print("                                                                ")
        print("********************************************************************************************")
        print("                                                                ")
        print("Trajet {}          {}                >>>>>>>>>>>>>>>>                {}".format(i+1, entry_villes[i], entry_villes[i+1]))
        print("---------------------------------------------------------------------------------------------")
        print("               Distance: {} kilomètres                        Durée: {}          ".format(distance_parcourue/1000, strftime('%H:%M', gmtime(temps_s))))
        distance_total += distance_parcourue
        temps_total += temps_s
    
    temps_total += 2700 * (len(entry_villes)-2)
    print("                                                                ")
    print("                                                                ")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("                                                                ")
    print("Total          {}                >>>>>>>>>>>>>>>>                {}".format(entry_villes[0], entry_villes[len(entry_villes)-1]))
    print("---------------------------------------------------------------------------------------------")
    print("               Distance total:    {} kilomètres                        Durée total: {}          ".format(distance_total/1000, strftime('%H:%M', gmtime(temps_total))))



        
multipleVille()