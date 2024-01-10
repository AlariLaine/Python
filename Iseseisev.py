# Iseseisev töö
# Alari Laine
# 18.12.23

# 1.1 Tervitus
def Tervita():
    print("Tere, maailm!")



# 1.2. Aasta liblikas
# 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
# 2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks &quot;teelehe- mosaiikliblikas&quot; (sõnena);
# 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks &quot;. aasta liblikas on &quot; (sõnena);
# 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
# 5. real väljastatakse muutuja lause väärtus ekraanile.
def liblikas():
    aasta = 2020
    liblikas = "teelehemosaiikliblikas"
    lause_keskosa = ". Aasta liblikas on "
    lause = (f"{aasta}{lause_keskosa}{liblikas}")
    print(lause)

"""
1.3. Pilved
Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi
pilvedeks. Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel,
alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
● küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
● väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
● väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
"""

def pilved(alus):
    if alus > 6:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")
    

"""
1.4. Bussid
Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid
on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi
kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu
inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
"""
def bussidearv(i, k):
    bussid = i % k
    if i == k:
        bussid = i // k
        viimases = i 
    elif bussid > 0:
        bussid = i // k + 1
        viimases = i % k
    else:
        bussid = i // k
        viimases = k
    print(f"Busse vaja: {bussid}. \nViimases bussis: {viimases} inimest")



Tervita()
liblikas()
alus = float(input("Pilvede aluse kõrgus (kilomeetrites):"))
pilved(alus)
inimesed = int(input("Inimeste arv: "))
kohti_bussis = int(input("Kohtade arv: "))
bussidearv(inimesed, kohti_bussis)
