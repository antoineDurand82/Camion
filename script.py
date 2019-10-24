from dictionnaire import villes
from math import *
import time



def livraison(depart, arrivee):
    vitesse_m = 0
    distance_trajet = villes[depart][arrivee] * 1000
    distance_parcourue = 0
    temps_s = 0
    t_avant_pause = 0
    pause = False
    nb_Pause = 0
    while (distance_parcourue < distance_trajet):

        if (t_avant_pause == 6660):
            pause = True
            

        if (pause == True):
            if (vitesse_m > 25/9):
                vitesse_m -= 25 / 9
                temps_s += 60
                distance_parcourue = vitesse_m * temps_s
            elif (vitesse_m < 25/9):
                temps_s += 900
                t_avant_pause = 0
                vitesse_m = 0
                pause = False
                nb_Pause += 1
        else:
            temps_s += 60
            t_avant_pause += 60
            distance_parcourue = vitesse_m * temps_s

        if (t_avant_pause < 600):
            if (vitesse_m < 25):
                vitesse_m += 25 / 9
                distance_parcourue = vitesse_m * temps_s

        print(t_avant_pause)
        print("Vitesse = " + str(vitesse_m))
        print("Distance = " + str(distance_parcourue))
        print("Temps = " + str(temps_s))
        print("Nombre de pause total = " + str(nb_Pause))
      
        
        
        

    
    
depart = input()
arrivee = input()
livraison(depart, arrivee)