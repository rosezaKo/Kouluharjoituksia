import random  # Valmis kirjasto

satunnaisluku = random.randint(1,6)
print(satunnaisluku)

print(random.random() * 100)
lista = [0,1,2,3,4,5,6,7,8,9]
print(random.choice(lista))






#Lotto simulaattori

#Käyttäjä valitsee 7 numeroa. väliltä 1-41,
#kaikkien lukejen tulee olla uniikkeja

#Simulaattori randomi soi 7kpl numeroita väliltä 1-41,
#kaikkien lukujen tulee olla uniikkeja

#Lopuksi ohjelma tulostaa oikein arvattujen lukujen määrän,
#ja jos kaikki on oikein niin tulostaa "Voitit"
Lotto = []
#valinta = int(input("Valitse 7 numeroa, 1-41 väliltä: "))

while(len(Lotto) < 7):
    luku = random.randint(1,41)
    if len(Lotto) == 7: