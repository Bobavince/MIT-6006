#Personnal import
from oneDPeakFinder import *
from twoDPeakFinder import *
from chrono import chrono
#Standard import
from random import randint
    
def main():
    #---- 1D part ----
    LARGEUR_TAB_1D = 15
 
    #Data Set
    data = [randint(0,99) for x in range (LARGEUR_TAB_1D)] #Total random
    data2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,19,18,17,16,15,14,12,10,5] #Linear progression
    
    #Allow the launch of the fonction with timing
    print("---------------------")
    chrono(launch1DStandardFinder, data2)
    chrono(launch1DEfficientFinder, data2)
    
    #---- 2D part ----
    LARGEUR_TAB_2D = 5
    data3 = [[randint(0,99) for x in range(LARGEUR_TAB_2D)] for y in range(LARGEUR_TAB_2D)]
    data4 = [[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16],[17,18,19,20,19,18,17,16],[15,14,12,10,5,7,8,9]] #Linear progression
    
    #Allow the launch of the fonction with timing
    print("---------------------")
    chrono(launch2DStandardFinder, data3)
    chrono(launch2DEfficientFinder, data3)

if __name__ == '__main__':
	main()


	