from math import *

#Ü6
print()
print("Ülesanne 6")
print()
for i in range(0,5):
    print("* "*5)
print()
for i in range(0,10):
    print("* "*i)
print()
for i in range(0,10):
    print("* "*(10-i))
print()
x=0
while x<5:
    print("* "*5)
    x+=1
x=0
print()
while x<10:
    print("* "*x)
    x+=1
x=11
print()
while x>0:
    print("* "*(x-1))
    x-=1

#Ü0
print()
print("Ülesanne 0")
print()
kujund=input("Vali kujund (ristkülik, rööpkülik, kolmnurk, ring) ").lower()
while kujund not in ["ristkülik", "rööpkülik", "kolmnurk", "ring"]:
    kujund=input("Palun kirjutage õige kujund! ").lower()
tegevus=input("Mis sa otsi? (pindala, perimeeter) ").lower()
while tegevus not in ["pindala","perimeeter"]:
    tegevus=input("Palun kirjuta õige tegevus! ").lower()
if kujund=="ristkülik":
    if tegevus=="pindala":
        a=input("Kirjuta 1 külg ")
        while a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        b=input("Kirjuta 2 külg ")
        while b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        S=float(a)*float(b)
        print("Pindala on ", S)
    else:
        a=input("Kirjuta 1 külg ")
        while a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        b=input("Kirjuta 2 külg ")
        while b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        P=2*(float(a)+float(b))
        print("Perimeeter on ",P)
elif kujund=="kolmnurk":
    if tegevus=="pindala":
        a=input("Kirjuta alus ")
        while a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige alus ")
        h=input("Kirjuta kõrgus ")
        while h.replace(".","",1).isdigit()==False:
                h=input("Kirjuta õige kõrgus ")
        S=(float(a)*float(h))/2
        print("Pindala on ", S)
    else:
        a=input("Kirjuta 1 külg ")
        while a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        b=input("Kirjuta 2 külg ")
        while b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        c=input("Kirjuta 3 külg ")
        if c.replace(".","",1).isdigit()==False:
            c=input("Kirjuta õige külg ")
        P=float(a)+float(b)+float(c)
        print("Perimeeter on ",P)
elif kujund=="rööpkülik":
    if tegevus=="pindala":
        a=input("Kirjuta 1 külg ")
        while a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        b=input("Kirjuta 2 külg ")
        while b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        S=float(a)*float(b)
        print("Pindala on ", S)
    else:
        a=input("Kirjuta 1 külg ")
        while a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        b=input("Kirjuta 2 külg ")
        while b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        P=2*(float(a)+float(b))
        print("Perimeeter on ",P)
else:
    if tegevus=="pindala":
        r=input("Kirjuta raadius ")
        while r.replace(".","",1).isdigit()==False:
            r=input("Kirjuta õige raadius ")
        S=pi*float(r)**2
        print("Pindala on ",S)
    else:
        r=input("Kirjuta raadius ")
        while r.replace(".","",1).isdigit()==False:
            r=input("Kirjuta õige raadius ")
        C=pi*float(r)*25
        print("Perimeeter on ",C)


#print("Ülesanne 10")
#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:
#        print(x, end=" ")
#    x+=1

#print("Ülesanne 17 ")
#try:
    #num_horiz=int(input("Siseta ruutude arv horisontaalselt =>> \n"))
    #num_horiz=randint(1,20)
#except:
    #print("Value Error")
#try:
    #num_vert=int(input("Siseta ruutude arv vertikalselt =>> \n"))
    #num_vert=randint(1,20)
#except:
    #print("Value Error")
#for y in range (num_vert):
    #for x in range(num_vert)
        #print("das", end=" ")
    #print()