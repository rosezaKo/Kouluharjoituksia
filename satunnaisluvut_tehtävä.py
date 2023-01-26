import random
#Satunnaisluku tehtävä 1.1
satunnaisluku = random.random() * 10
print(satunnaisluku)

#tehtävä 1.2
satunnaisluku = random.random() * 2 - 1 
print(satunnaisluku)

#tehtävä 1.3
satunnaisluku = random.random() * 100
print(satunnaisluku, "%")

#tehtävä 1.4

arvaus = float(input("Valitse luku 0 tai 1: "))
satunnaisluku = random.random() * 1
if arvaus == 0 and satunnaisluku < 0.5:
    print("Voitit")
if arvaus == 0 and satunnaisluku > 0.5:
    print("Hävisit")
if arvaus == 1 and satunnaisluku > 0.5:
    print("Voitit")
if arvaus == 1 and satunnaisluku < 0.5:
    print("Hävisit")
print(satunnaisluku)

#Tehtävä 2.1
kokonaisluvut = random.randint(1,100)
print(kokonaisluvut)
#Tehtävä 2.2

noppapeli = input("START PRESS A!")
noppapelin_random = random.randint(1,6)
if noppapelin_random == 6:
    print("Voitit")
else:
    print("Hävisit")
print(noppapelin_random)

#Tehtävä 2.3
tulostus = 0
laskuri = 0
while laskuri < 100:
    print(laskuri)
    tulostus += 1
    laskuri += random.randint(1,6)
print("Tällä määrällä kasvatit lukua: ", tulostus)

#Tehtävä 2.4
laskuri1 = 0
tulostus1 = laskuri1 - random.randint(1,6)

while laskuri1 < 10:
    print(laskuri1)    
    laskuri1 += random.randint(1,6)
    
    


#Tehtävä 3.1
lista = ["Hillevi hiiri", "Pikku kakkonen", "Makaroonisoossi"]
listat = random.choice(lista)
print(listat)

#Tehtävä3.2
thislist = ["apple","banana","orange"]
while len(thislist) >= 1:
    this = thislist.remove(random.choice(thislist))
    print(thislist)

#Tehtävä 3.3
maara = 0
ekalista = []
tokalista = []
for i in range(1,101):
    ekalista.append(i)
    
while 7 not in tokalista:
    num = random.choice(ekalista)
    tokalista.append(num)
    ekalista.remove(num)
    maara += 1    
print(tokalista)
print("Määröjä oli: ", maara)
#Tehtävä 3.4
munlista = ["markus","tikru","miisu","kebab","mörkö","aapo","jere","max","freak","juuso"]
toinenlista = []
laskurini = 0
while laskurini <= 40:
    toinenlista.append(random.choice(munlista))
    laskurini += 1
print(toinenlista)


