#tehtävä1,1
def kahdenParametrinFunktio(data1,data2):
    print(data1 + " " + data2)
kahdenParametrinFunktio("Tikru", "Miisu")

#tehtävä1,2
def kolmenParametrinFunktio(miisu1,miisu2,miisu3):
    print((miisu1 + miisu2 + miisu3) / 3)
kolmenParametrinFunktio(5,5,5)

#tehtävä1,3

def numbers(x):
    for i in x:
        if i % 2 == 0:
            print(i)
lista = [2,3,5,7,5,6,2,4]
numbers(lista)

#tehtävä 1,4
def numbers1(v):
    for c in v:
        if c % 2 == 1:
            print(c)
lista1 = [2,3,5,7,5,6,2,4]
numbers1(lista1)

#tehtävä 2.1

def yhdenSuurempi(v,b):
    print(v + 1, b + 1)
v = int(input("Say one number: "))
b = int(input("Say one number: "))
yhdenSuurempi(v,b)

#tehtävä 2.2
v = int(input("v = "))
def positive(v):
    print(v + v * -2)
positive(v)
#tehtävä2,3
def big(a):

    res = a[0]
    for i in a:
        if res < i:
            res = i
    return res

array = (1, 2, 3, 9, 5, 6)

print(big(array))

def big2(y):

    res1 = y[0]
    for f in y:
        if res1 > f:
            res1 = f
    return res1

array1 = (1, 2, 3, 4, 5, 6)

print(big2(array1))

def big3(a2):

    res3 = a2[0]
    for d in a2:
        if res3 < d:
            res3 = d
    return res3

array2 = (1, 2, 3, 4, 5, 6)

print(big3(array2))

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("Keskiarvo on ", cal_average([8,2,3,4,5,6]))


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 20

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
