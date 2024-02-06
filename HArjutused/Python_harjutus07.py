# Massiivid - Array
# 5.12.23
# Alari Laine
import math

def tervita(nimi, keel="de"):
    if keel == "en":
        print(f"Hi {nimi}!")
    elif keel == "et":
        print(f"Tere {nimi}!")
    else:
        print(f"Hallo {nimi}!")

tervita("Jaanus")
tervita("Jaanus", "en")


def kera(r):
    v = round(4*math.pi*r**2,2)
    print(f"Kera ruumala on: {v} ")


def kuup(a,b,c):
    v = a*b*c
    print(f"Kuubi rummala on: {v}")

def koonus():
    pass

def silinder():
    pass

loop = 1
print("--------------------KUJUNDI VALIMINE-----------------")
while loop == 1:
    print("Vali kujund: \n1. Kera \n2. Kuup \n3. Koonus \n4. Silinder \n5. EXIT\n-------------- ")
    valikujund  = int(input("Vali Kujund:"))

    if valikujund == 1:
        r = int(input("Raadius: "))
        kera(r)
    elif valikujund == 2:
        a = int(input("Külg 1: "))
        b = int(input("Külg 2: "))
        c = int(input("Külg 3: "))
        kuup(a,b,c)

    elif valikujund == 3:
        koonus()

    elif valikujund == 4:
        silinder()
    else:
        loop = 0
        print("\n------------------------------")


print("buh bye")

