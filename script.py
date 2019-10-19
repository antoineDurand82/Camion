from dictionnaire import villes
import math



def livraison(depart, arrivee):
    vitesse_m = 0
    distance_trajet = villes[depart][arrivee] * 1000
    distance_parcourue = 0
    temps_s = 0
    while (distance_parcourue != distance_trajet):
        while (vitesse_m != 90000):
            vitesse_m += 10000
            distance_parcourue += vitesse_m / 3600
            temps_s += distance_parcourue / (vitesse_m / 3600)
            
        distance_parcourue += vitesse_m / 3600
        temps_s += distance_parcourue / (vitesse_m / 3600)
        print(distance_parcourue)
        print(temps_s / 60)
      
        
        
        

    
    
depart = input()
arrivee = input()
livraison(depart, arrivee)