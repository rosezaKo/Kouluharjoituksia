foo = [23,46,"moro"]

#listan läpikäynti
for f in foo:
    print(f)
    
#for in rangella sama
    
for f in range(len(foo)):
    print(foo[f])

#rautalankallani
    
laskuri = 0
while laskuri < len(foo):
    print(foo[laskuri])
    laskuri += 1