import random

class Perusolio:
    def __init__(self):
        self.nimi = "eioleviela"
        self.x = None
        self.y = None

    
    def juoksee(self):
        print("Huhhuh, juoksen torille vauhdilla!")

class Hyttynen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.puremisvoima = random.randint(5, 15)
    
    def liiku(self):
        suunta = random.choice(["ylös", "alas", "vasen", "oikea"])
        if suunta == "ylös":
            self.y -= 1
        elif suunta == "alas":
            self.y += 1
        elif suunta == "vasen":
            self.x -= 1
        else:
            self.x += 1

class Aarre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.suuruus = random.randint(50, 100)

class Este:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pelikentta:
    def __init__(self):
        self.koko = 10
        self.ihminen = Perusolio()
        self.ihminen.nimi = "Pelaaja"
        self.hyttyset = []
        self.aarre = None
        self.estee = None
        self.ruudukko = [[[] for _ in range(self.koko)] for _ in range(self.koko)]
    
    def aseta_oliot(self):
        # Asetetaan pelaaja
        self.ruudukko[random.randint(0, self.koko-1)][random.randint(0, self.koko-1)].append(self.ihminen)
        
        # Asetetaan hyttyset
        for _ in range(10):
            x = random.randint(0, self.koko-1)
            y = random.randint(0, self.koko-1)
            hyttynen = Hyttynen(x, y)
            self.hyttyset.append(hyttynen)
            self.ruudukko[x][y].append(hyttynen)
        
        # Asetetaan aarre
        x = random.randint(0, self.koko-1)
        y = random.randint(0, self.koko-1)
        self.aarre = Aarre(x, y)
        self.ruudukko[x][y].append(self.aarre)
        
        # Asetetaan este
        x = random.randint(0, self.koko-1)
        y = random.randint(0, self.koko-1)
        self.estee = Este(x, y)
        self.ruudukko[x][y].append(self.estee)
    
    def piirra_ruudukko(self):
        for rivi in self.ruudukko:
            for ruutu in rivi:
                if self.ihminen in ruutu:
                    print("P", end=" ")
                elif self.aarre in ruutu:
                    print("A", end=" ")
                elif any(isinstance(olio, Hyttynen) for olio in ruutu):
                    print("H", end=" ")
                elif self.estee in ruutu:
                    print("E", end=" ")
                else:
                    print("-", end=" ")
            print()
    
    def tarkista_tilanne(self):
        # Tarkistetaan pelaajan energia
        if self.ihminen.energia <= 0:
            return "häviö"
        
        # Tarkistetaan pelaajan sijainti
        x = self.ihminen.x if hasattr(self.ihminen, 'x') else None
        y = self.ihminen.y if hasattr(self.ihminen, 'y') else None


        ruutu = self.ruudukko[x][y]
        
        # Tarkistetaan törmäykset
        for olio in ruutu:
            if isinstance(olio, Hyttynen):
                self.ihminen.energia -= olio.puremisvoima
                self.hyttyset.remove(olio)
                ruutu.remove(olio)
        
        # Tarkistetaan voitto
        if self.aarre.x == x and self.aarre.y == y:
            return "voitto"
        
        return "jatkuu"
    
    def pelaa(self):
        self.aseta_oliot()
        x = 0  # Alustus
        y = 0  # Alustus
        while True:
            self.piirra_ruudukko()
            
            # Pelaajan siirto
            suunta = input("Mihin suuntaan haluat liikkua? (wasd/nuoli): ")
            self.ihminen.x = x if hasattr(self.ihminen, 'x') else 0
            self.ihminen.y = y if hasattr(self.ihminen, 'y') else 0


            if suunta == "w" or suunta == "ylös":
                y -= 1
            elif suunta == "s" or suunta == "alas":
                y += 1
            elif suunta == "a" or suunta == "vasen":
                x -= 1
            elif suunta == "d" or suunta == "oikea":
                x += 1

            
            # Tarkistetaan siirron validius
            if x < 0 or x >= self.koko or y < 0 or y >= self.koko:
                print("Virheellinen siirto!")
                continue
            
            # Tarkistetaan este
            if self.ruudukko[x][y] and self.estee in self.ruudukko[x][y]:
                print("Este!")
                continue
            
            # Päivitetään pelaajan sijainti
            self.ruudukko[self.ihminen.x][self.ihminen.y].remove(self.ihminen)
            if x is not None:
                self.ihminen.x = x
            if y is not None:
                self.ihminen.y = y
            self.ruudukko[x][y].append(self.ihminen)

            
            # Liikutetaan hyttysiä
            for hyttynen in self.hyttyset:
                self.ruudukko[hyttynen.x][hyttynen.y].remove(hyttynen)
                hyttynen.liiku()
                self.ruudukko[hyttynen.x][hyttynen.y].append(hyttynen)
            
            # Tarkistetaan pelitilanne
            tilanne = self.tarkista_tilanne()
            if tilanne == "häviö":
                print("Pelaaja hävisi!")
                break
            elif tilanne == "voitto":
                print("Pelaaja voitti!")
                break


# Pelin käynnistys
peli = Pelikentta()
peli.pelaa()
