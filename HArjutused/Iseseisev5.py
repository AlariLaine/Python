# Alari Laine   
# Iseseisev 5


import random








#1. Korrutamise kontrollimine
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

#3. Positiivsete ja negatiivsed

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

#5. Shopping list

shopping_list = []

while True:
    item = (input("Sisesta toode: "))
    if item == "":
        break
    else:
        shopping_list.append(item)
print(shopping_list)


#7. Eurokalkulaator
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


#9. Emaili kontrollimine

#kysib kasutajalt emaili
email_kontroll = input("Sisesta email kujul enimi.pnimi@server.com: ")
#kui emailis on "@" ja "." siis prindib tere ja emaili serveri ja domeeni
if "@" in email_kontroll:
    #võtab emaili enne "@" ja prindib selle suure algustähega
    print("Tere, " + email_kontroll.split("@")[0].split(".")[0].capitalize() +","+" sinu email on server serveris ja domeeniks on sul com")
else:
    #kui emailis pole "@" ja "." siis prindib et email on valesti sisestatud
    print("Email on valesti sisestatud!")
    
    
#11. Salakeel

#kysib kasutajalt kas ta soovib salakeelt luua või tõlkida
tolkimine = input("Valige kas 1. Salakeele loomine või 2. Salakeele tõlkimine: ")

#kui kasutaja valib 1 siis ta saab luua salakeele
if tolkimine == "1":
    #kysib kasutajalt sõna
    Salakeel = input("Sisesta sõna: ").lower()
    #prindib sõna vastavalt kuidas on tahetud, et tähed asendatakse
    print(Salakeel.replace("a", "e").replace("o", "u").replace("i", "o").replace("e", "i").replace("u", "a"))
    #kui kasutaja valib 2 siis ta saab tõlkida salakeelt
elif tolkimine == "2":
    #siin samamoodi nagu 1 aga vastupidi
    Salakeel = input("Sisesta sõna: ").lower()
    print(Salakeel.replace("e", "a").replace("u", "o").replace("o", "i").replace("i", "e").replace("a", "u"))
else:
    #kui kasutaja valib midagi muud siis prindib et valik on vale
    print("Vale valik!")

#13. paaritu või paaris
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
    
    
    
#15. Temperatuurid
temperatuurid = {
    "jaanuar": [-16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3],
    "veebruar": [-9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18],
    "märts": [2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2],
    "aprill": [-5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2],
    "mai": [12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1],
    "juuni": [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22],
    "juuli": [15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20],
    "august": [7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11],
    "september": [21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19],
    "oktoober": [2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1],
    "november": [-6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1],
    "detsember": [-15, 2, -11, -14, -15, -5, -5, -18, -18, -19, 0, 0, 2, -7, -16, -7, -4, -1, -1, -16, -18, -10, -3, -19, -6, -16, -16, -8, -2, -18]
}

def soojempaev(temperatuurid):
    esimene_kuu = list(temperatuurid.values())[0]
    soojem_kuu = ""
    soojem_paev = 0
    max_temp = esimene_kuu[0]

    for kuu, temperatuurid_kuus in temperatuurid.items():
        for päev, temp in enumerate(temperatuurid_kuus, start=1):
            if temp > max_temp:
                max_temp = temp
                soojem_kuu = kuu
                soojem_paev = päev
    
    print(f"Kõige soojem päev oli {soojem_paev}.{soojem_kuu} temperatuuriga {max_temp} kraadi.")

soojempaev(temperatuurid)

#17. Emaili kontrollimine

def kontrolli_email():
    email_kontroll = input("Sisesta email kujul enimi.pnimi@server.com: ")

    if "@" in email_kontroll and "." in email_kontroll:
        nimi, domeen = email_kontroll.split("@")
        eesnimi = nimi.split(".")[0]
        server, com = domeen.split(".")
        print(f"Tere {eesnimi.capitalize()}, sinu email on server {server} ja domeeniks on sul {com}")
    else:
        print("Email on valesti sisestatud!")

kontrolli_email()