def palauttaaKolmenArgumentinSumma (z,x,n):
    print(z + x + n)
palauttaaKolmenArgumentinSumma(5,5,5)

n = input("What is your name?:")
def name(n):
    print("Hello " + n)
name(n)


s = input("Mikä salasanasi")
x = 1234

if s == x:
    print("Password is correct!")
else:
    print("Password is incorrect")

print("Kolmion pinta-ala")
a = int(input("Mikä on pituus? "))
c = int(input("Mikä on korkeus? "))

def ac(c):
    print(c * a)
ac(c)

print("Neliön pinta-ala")
g = int(input("Mikä on korkeus? "))

def ab(g):
    print(g * 4)
ab(g)

print("Ympyrän pinta-ala")
h = int(input("Mikä on pituus? "))
j = int(input("Mikä on korkeus? "))
def az(h):
    print(h * j)
az(h)

print("Suorakulmion pinta-ala")
g = float(input("Mikä on säde? "))
def ad(g):
    print(g * g * 3,14)
ad(g)

import random
k = random.randint(10,40)
print(k)
o = int(input("Arvaa luku luvuilta 10-40: "))

if o == k:
    print("Good job!")
elif o != k:
    print("Wrong answer")
if o < 10:
    print("Too little")
elif o > 40:
    print("Too big")








