# Alari Laine   
# Iseseisev 5


import random

# paaritu või paaris
try:
    arv = int(input("Sisesta arv: "))
    if arv == 0:
        print("Arv on null")
    elif arv == "":
        input(print("Arv puudub"))
    elif arv % 2 == 0:
        print("Arv on paaris")
    else:
        print("Arv on paaritu")
except ValueError:
    print("Arv peab olema number")

# Korrutamise kontrollimine

def korrutamine(a, b):
    vastus = int(input(f"{a} * {b} = "))
    if vastus == a*b:
        print("Õige!")
    else:
        print("Vale!")
        print(f"Õige vastus on {a*b}")
    

for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    korrutamine(a, b)


# Positiivsete ja negatiivsed

positiivsed = []
negatiivsed = []

arv = 0

for i in range(5):
    arv = int(input("Sisesta arv: "))
    if arv > 0:
        positiivsed.append(arv)
    elif arv < 0:
        negatiivsed.append(arv)
    else:
        print("Null ei lähe kuhugi")
        

print(f"Positiivsed: {positiivsed}")
print(f"Negatiivsed: {negatiivsed}")

# Shopping list

shopping_list = []

while True:
    item = (input("Sisesta toode: "))
    if item == "":
        break
    else:
        shopping_list.append(item)
print(shopping_list)


# Eurokalkulaator
# Küsib kasutajalt valiku, kas ta soovib teha eurokalkulatsiooni või kroonikalkulatsiooni
kalkulaatori_valik = input("Vali kalkulaator: 1. Eurokalkulaator, 2.Kroonikalkulaator: ")
# Kui kasutaja valib 1, siis ta soovib teha eurokalkulatsiooni
if kalkulaatori_valik == "1":
    eurokalkulaator = ()
    # Küsib eurode arvu
    euro = float(input("Sisesta eurod: "))
    # Arvutab eurod kroonideks
    eesti_kroon = euro * 15.6466
    print(f"{euro} eurot on {eesti_kroon} krooni")
# Kui kasutaja valib 2, siis ta soovib teha kroonikalkulatsiooni
elif kalkulaatori_valik == "2":
    kroonikalkulaator = ()
    # Küsib kroonide arvu
    kroon = float(input("Sisesta kroonid: "))
    # Arvutab kroonid eurodeks
    euro = kroon / 15.6466
    print(f"{kroon} krooni on {euro} eurot")
else:
    # Kui kasutaja valib midagi muud, siis ta saab veateate
    print("Vale valik!") 


# Emaili kontrollimine


email_kontroll = input("Sisesta email kujul enimi.pnimi@server.com: ")

if "@" in email_kontroll:
    print("Tere, " + email_kontroll.split("@")[0].split(".")[0].capitalize() +","+" sinu email on server serveris ja domeeniks on sul com")
else:
    print("Email on valesti sisestatud!")
    
    
# Salakeel

tolkimine = input("Valige kas 1. Salakeele loomine või 2. Salakeele tõlkimine: ")


if tolkimine == "1":
    Salakeel = input("Sisesta sõna: ").lower()
    print(Salakeel.replace("a", "e").replace("o", "u").replace("i", "o").replace("e", "i").replace("u", "a"))
elif tolkimine == "2":
    Salakeel = input("Sisesta sõna: ").lower()
    print(Salakeel.replace("e", "a").replace("u", "o").replace("o", "i").replace("i", "e").replace("a", "u"))
else:
    print("Vale valik!")