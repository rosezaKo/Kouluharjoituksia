class auto():
    merkki = ""
    vuosi = 0
    vari = ""
    
    def vaihdavari(self,newcolor):
        self.vari = newcolor
        
    
Martin = auto()
Martin.merkki = "Mersu"
Martin.vuosi = 1994
Martin.vari = "Tummansininen"
Martin.vaihdavari("Punainen")
print(Martin.merkki)
print(Martin.vuosi)
print(Martin.vari)
print(Martin.vaihdavari)

