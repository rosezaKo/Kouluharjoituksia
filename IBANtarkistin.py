def tarkista_tilinumero(tilinumero):
    # Poista välilyönnit ja tarkista pituus
    tilinumero = tilinumero.replace(" ", "")
    if len(tilinumero) != 18:
        return False
    
    # Siirrä maatunnus ja tarkistenumero loppuun
    tilinumero = tilinumero[4:] + tilinumero[:4]
    
    # Korvaa kirjaimet numeroilla
    numerot = ""
    for merkki in tilinumero:
        if merkki.isalpha():
            numerot += str(ord(merkki.upper()) - 55)
        else:
            numerot += merkki
    
    # Laske jakojäännös
    jakojäännös = int(numerot) % 97
    
    # Palauta True, jos jakojäännös on 1, muuten False
    return jakojäännös == 1
# FI42 5000 1510 0000 23
# Pyydä tilinumeroa käyttäjältä
tilinumero = input("Syötä tilinumero: ")
tulos = tarkista_tilinumero(tilinumero)
print(tulos)
