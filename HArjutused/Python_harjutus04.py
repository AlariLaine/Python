import random
# Alari Laine
# 21.11.2023
# Ülesanne 4

# Ruutude ja kuupide tabel
print("Arv  Ruut  Kuup")
for i in range(1,11):
    print(f"{i}{i**2:6}{i**3:8}")



input()
# Pank

raha = 10000
aasta = 5
konto = raha
intress = 0.05



print("Aasta   Algsumma    Intress    Aasta lõpuks")
for i in range(aasta):
    print(f"{i+1} {konto:14.2f} {konto*intress:9.2f}{konto + konto * intress:13.2f}")
    konto = konto + konto * intress

print(f"Summa kokku: {konto:.2f}€")
print(f"Kasum: {konto-raha:10.2f}€")

input()

# arvamismäng WHILE + FOR
loop = 1
voidud = 0

while loop == 1:
    print("-------------Arvamismäng-----------")
    suv = random.randint(1,3)
    print(suv)
    for i in range(3):
        arva = int(input("Paku arv 1-100: "))
        if suv == arva:
            print("Arvasid ära!")
            voidud += 1
            break
        else:
            print("Proovi uuesti")
    print("------------GAME OVER--------------")
    print(f"Võidud: {voidud}")
    jatka = input("soovid jätkata? y/n: ")
    if jatka == "n":
        loop = 0
    
# viisikud    

for i in range(1,101):
    if i%5 == 0:
        print(i)

input()

# Korrutustabel

for j in range(1,11):
    for i in range(1,11):
        print(f"{j} x {i} = {j*i}")

#paaris/pparitu

for x in range(1,11):
    if x % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
    print(x,v)

# jalgapall

sugu = "m"
if sugu == "m":
    vanus = 17
    if vanus >= 16 and vanus <= 18:
        print("Tere tulemast")
    else:
        print("Vanus ei sobi")
else:
    print("ei pääase meeskond")

#tärn
j = 5
for i in range(j):
    print("*"*(i+1))
j = 5
for i in range(5):
    print("*"*j)
    j = j - 1
print()
j = 5
for i in range(j):
    print("*"*j)


# loto

for x in range(5):
    print(random.randint(0,9),end="")

print()

# müük

hind = 9
if hind <= 10:
    vastus = 0.1
    
else:
    hind >= 10
    vastus = 0.2
print(hind - hind * vastus)

# juubel
v = int(input("Sisesta sünnipäev: "))
if v % 5 == 0:
    vastus = "on"
else:
    vastus = "ei ole"
print(f"vanus {v}: {vastus} juubel")


"""
Matemaatika
    Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
    Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
nr1 = int(input("arv 1: "))
nr2 = int(input("arv 2: "))
tehe = input("Vali tehe + - * / ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = round(nr1 / nr2, 2)
else:
    vastus = "Ära pulli mees!"

print(f"{nr1} {tehe} {nr2} {vastus}")
"""
Ruut
    Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
    Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
nr1 = int(input("ruudu 1. külg: "))
nr2 = int(input("ruudu 2. külg: "))

if nr1 == nr2:
    print("ruut")
else:
    print("mingi muu asi")