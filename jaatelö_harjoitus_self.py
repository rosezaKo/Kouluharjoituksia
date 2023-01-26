class Tuuppi:
    def __init__(self):
        self.tuuppi = "Sorbetin"
        self.maara = 100
class Jaatelo:
    def __init__(self):
        self.maukkuus = []
        self.maku = "entieda"
        self.vatsa = []
        self.nalka = 200
    def nauttiminen(self):
        print("Nam,nam...")
    def syonti(self,jatelo):
        self.vatsa.append(jatelo)
        self.nalka -= jatelo.maara
        jatelo.maara = 0
        
        
sorbetti = Tuuppi()        
jaateloni = Jaatelo()
jaateloni.maku = "Chocolate"
jaateloni.nauttiminen()
jaateloni.syonti(sorbetti)
print("Minkälaisen jäätelön haluat?", sorbetti.tuuppi)
print("Jäätelön maku on",jaateloni.maku)
print("Minun nälkäni on",jaateloni.nalka)
print("Jaatelön määrä on:",sorbetti.maara)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
class Kattila:
    def __init__(self):
        self.maara = 1
        self.puhtaus = "puhdas"
        self.nimi = "Teräs kattila"
        self.mukavuus = "hyvä"
        paino = 500
    def vedenmaara(self):
        self.vedenmaara = 400
        
    def materiaali(self):
        self.material = "ruostumaton teräs"
        self.laatu = "En vielä tiedä"
        