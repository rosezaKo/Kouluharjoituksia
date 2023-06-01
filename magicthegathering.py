def HasEnoughMana(Manapool,cost):
#     Laskee numeroiden määrän
    NumeroSymboleita = 0
    for i in range(len(cost)):
        if cost[i].isdigit() == True:
            NumeroSymboleita += 1
            
#     Määrittelee numerollisen hinnan ja värillisen hinnan.
    Neutraalihinta = 0
    if NumeroSymboleita > 0:
        Neutraalihinta = int(cost[0:NumeroSymboleita])
        Neutraalihinta = int(Neutraalihinta)
    Värihinta = list(cost[NumeroSymboleita:])
    
    print(Värihinta)
    # Onko värihinta maksettavissa.
    
    for i in range(len(Värihinta)): #Manapool = RGG
        if Värihinta[i] in Manapool: # Cost = RRG
            Manapool = Manapool.replace(Värihinta[i],"",1)
            
        else:
            return False
    print(Manapool)
    
    #Tarkistaa neutraalin manan
    if len(Manapool) < Neutraalihinta: # Ei ole tarpeeksi manaa
        return False
    return True
    
print(HasEnoughMana("RGUBWC","3RG")) #True
print(HasEnoughMana("WWBB","WWW")) # False
print(HasEnoughMana("RRR","3")) # True
print(HasEnoughMana("RGG","GRR")) # False