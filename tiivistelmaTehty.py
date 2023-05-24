import random

# MUUTTUJAT
a = 12
b = 1.5
c = "Norsu"
d = [1, 2, 3, 1]
a, b = c, d

# FUNKTIOT
def kissaprintti():
    print("Kissa")

def sanaprintti(sana):
    print(sana)

def summa(a, b):
    return a + b

# JAKOJAANNOS
print(6 % 4)

# Toistorakenne
laskuri = 0
while laskuri < 10:
    print(laskuri, end=" ")
    laskuri = laskuri + 1

# Toistorakenne, joka lukee taulukkoa
kissat = ["Appe", "Benita", "Cissa", "Diisu"]
laskuri = 0
while laskuri < len(kissat):
    print(kissat[laskuri])
    laskuri = laskuri + 1

# Taulukon lopusta alkuun lukeminen
laskuri = len(kissat) - 1
while laskuri >= 0:
    print(kissat[laskuri])
    laskuri = laskuri - 1

# Taulukon läpikäynti ja uuden taulukon luominen
kissat_paino = []
laskuri = 0
while laskuri < len(kissat):
    kissat_paino.append(kissat[laskuri])
    kissat_paino.append(laskuri + 1)
    laskuri = laskuri + 1
print(kissat_paino)

# Numeroiden summaaminen taulukosta
numerot = [3, 4, 5, 6, 7, 12]
summa = sum(numerot)
print("Summa:", summa)

# Lisää numerot-taulukon loppuun kymmenen kappaletta numeroa 5
laskuri = 0
while laskuri < 10:
    numerot.append(5)
    laskuri = laskuri + 1
print(numerot)

# Funktio taulukon kääntämiseen
def kaanna(taulukko):
    kaannetty = []
    indeksi = len(taulukko) - 1
    while indeksi >= 0:
        kaannetty.append(taulukko[indeksi])
        indeksi = indeksi - 1
    return kaannetty

tulos = kaanna(numerot)
print("Käännetty taulukko:", tulos)

# Satunnaisen parillisen luvun generointi
def parillinen(x, y):
    luku = random.randint(x, y)
    if luku % 2 != 0:
        luku = luku + 1
    return luku

parillinen_luku = parillinen(1, 10)
print("Satunnainen parillinen luku:", parillinen_luku)

# OLIOT, CLASS ja SELF
class Kissa:
    def __init__(self):
        self.nimi = "eivielanimea"
        self.jalat = 4
        self.pennut = []

    def naukuminen(self):
        print("Miau")

munkissa = Kissa()
munkissa.nimi = "Miisu"

# TIEDOSTON KIRJOITUS
f = open("testi.txt", "w")
f.write("Miisu")
f.close()

# TIEDOSTOSTA LUKU
f = open("testi.txt", "r")
teksti = f.read()
f.close()
print("Tiedostosta:", teksti)
