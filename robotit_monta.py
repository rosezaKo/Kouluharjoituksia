import random

class Maailma:
    def __init__(self):
        self.vihut = []
        self.keskiarvo = 0
        self.Napoleon = Hahmo()
        self.Napoleon.tyyppi = "Sankari"
        self.Napoleon.stamina = 300

    def aikatikki_staminankulutus(self):
        for vihu in self.vihut:
            vihu.stamina += 1
        # Laske elossa ja kuolleet ja printtaa ne
            
    def sankari_tuhopoly(self):
        self.Napoleon.stamina -= 30
        # Kun tätä metodia kutsutaan, puolille vihuista stamina vähenee 10
        # Jos näiden vihujen stamina on alle 0, ne kuolevat!
        
        # Tai satunnaisesti joka toista
        for vihu in self.vihut:
            if random.randint(0, 1) == 0:
                vihu.staminanmuutos(-10)
    
    def sankari_pakenee(self):
        # Arvotaan satunnainen pako-onnistuminen
        pako_onnistui = random.randint(0, 1) == 0

        if pako_onnistui:
            print("Sankari pakeni onnistuneesti!")
            # Tässä voit toteuttaa pako-toiminnallisuuden ja sen seuraukset
        else:
            print("Sankari ei onnistunut pakenemaan!")
            # Tässä voit toteuttaa seuraukset, jos pako epäonnistui

class Hahmo:
    def __init__(self):
        self.stamina = random.randint(10, 50)
        self.tyyppi = "Vihu"
        self.elossaVaiEi = "Elossa"
        
    def staminanmuutos(self, muutosmaara):
        self.stamina += muutosmaara
        if self.stamina <= 0:
            self.elossaVaiEi = "Kuollut"
            
munmaailma = Maailma()

for _ in range(100):
    tmphahmo = Hahmo()
    munmaailma.vihut.append(tmphahmo)

while munmaailma.Napoleon.stamina > 100:
    munmaailma.aikatikki_staminankulutus()
    toimenpide = input("Mitä sankari tekee? Pakenee (p) vai heittää tuhopolya (t)?")
    if toimenpide == "t":
        munmaailma.sankari_tuhopoly()
    if toimenpide == "p":
        munmaailma.sankari_pakenee()
