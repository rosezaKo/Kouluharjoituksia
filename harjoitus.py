#muuttuja = variable
kissa = 5
print(kissa)
kissa = 7
print(kissa)

#Lainaus merkit osoittaa asian olevan tekstiä
nimi = "miisu" # "" = string
print(nimi)
#teksti ja numerot yhdistyvät eri tavalla
koira = 6
aasi = "6"

print(koira + koira)
print(aasi + aasi)

kokonaisluku = 1 # integer -> int
desimaaliluku = 1.4 # float, double


Lassi = 17
Olavi = 16

if Lassi == Olavi:
    print("Pojat ovat samanikäisiä")

if Lassi < Olavi:
    print("Lassi on nuorempi")
if Lassi > Olavi:
    print("Lassi on vanhempi")
    
# == yhtäsuurikuin
# > suurempikuin
# < pienempikuin
# >= suurempi tai yhtäsuurikuin
# <= pienempi tai yhtäsuurikuin
# != erisuurikuin


## Tehtävä
#Olet portsari.
#Asiakas haluaa sisään
#Vain täysi-ikäiset pääsevät sisään
#Täysi ikäistä tervehditään
#Alaikäinen käsketään poistumaan

asiakas = 16


if asiakas >= 18:
    print("Tervetuloa")
if asiakas < 18:
    print("Poistukaa täältä.")

#Toisto lause -> loop
    
for i in range(1,11):
    print(3 * i)
laskuri = 0
while laskuri < 10:
    print(laskuri * 4)
    laskuri += 1
    
    
    
#Silakat
#Miisulla on 10 silakkaa.
#Tee toistolause, joka vähentää silakoita yhden kerrallaan
#kun silakat loppu, niin tulosta "Pitaa ostaa lisää silakoita"

silakat = 10
while silakat > 0:
    print(silakat)
    silakat -=1
print("Pitää ostaa lisää silakoita")
if True:
    print("True")
    print("Miisu")
print("False")


def Tiikeri():
    print("Tiikeri")
    print("Bengalintiikeri")
    print("Tiikeritaistelu")
Tiikeri()

def YhdenIsompi(luku):
    print(luku + 1)
YhdenIsompi(5)


def YhdenPienempi(luku):
    return luku - 1
hevonen = YhdenPienempi(15)
print(hevonen)
muuli = YhdenPienempi(-100)
print(muuli)

#Funktio harjoitus
# Kirjoita funktio, joka laskee argumentin etäisyyden numerosta 100
luku = int(input("Sano, joku numero etäisyys numerosta 100 (numero): "))
def etaisyysNumerosta(luku):
    if luku > 100:
        return luku -100    
    if luku < 100:
        return 100 - luku
veikkaus = etaisyysNumerosta(luku)
print(veikkaus)

def Eta(luku):
    tulos = 100 - luku
    if tulos < 0:
        tulos *= -1
    return tulos


arvosana1 = 1
arvosana2 = 5
#...

arvosana = [1,5,4,3,5,8,5,3,2,5]
print(arvosana) # tulostaa kaikki
print(arvosana[0])
print(arvosana[1])


#len(arvosana) -> 10
for i in range(len(arvosana)):
    print(arvosana[i])
    
    


class auto():
    merkki = ""
    vuosi = 0
    vari = ""

Martin = auto()
    
    
    
    
    
    
 #tehtävä 1,1    
laskuri1 = 0
while laskuri1 < 21:
    print(laskuri1)
    laskuri1 += 1

#tehtävä 1.2
laskuri = 10
while laskuri < 21:
    print(laskuri)
    laskuri += 1

#tehtävä1.3
laskuri2 = 100
while laskuri2 > -1:
    print(laskuri2)
    laskuri2 -= 1
    
#tehtävä1.4
    
for i in range(1,10,2):
    print(i)
    
#tehtävä2.1
lista = ["omena","päärynä","kirsikka","appelsiini","banaani"]
for i in range(len(lista)):
    print(lista[i])
    
#tehtävä2.2
lista2 = [17,18,28,44,32,20]
for i in range(len(lista2)):
    if (lista2[i]) >= 18:
        print("täysi-ikäinen")
    else:
        print("alaikäinen")

#tehtävä2.3
for i in range(1,11):
    print(5 * i)
    
#tehtävä2.4
    
lista3 = ["tikru","miisu","kisu","rusina"]
lista3.reverse()
for i in range(len(lista3)):
    print(lista3[i])



    
    
