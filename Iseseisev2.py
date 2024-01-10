# Alari Laine
# 18.12.23
import random

# Äratus

def aratus(nr):
    for i in range(nr):
        print("Tõuse ja sära!")


# Murelikud lapsevanemad
def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid+=joostud_ringid
    print(f"Jänkulaps saab: {porgandid}, porgandit!")





# Täring

def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))




# Male

def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut <arv:
        nisuterad = nisuterad*2
        ruut+=1
    print(f"Nisuteri {ruut}. ruudu eest: {nisuterad}")



# Õunad
    
def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad -= pounad
        print(pounad)
    print(f"Lumivalgekesele jäi {ounad} õuna")













kordus = int(input("Sisestage mitu korda äratada: "))
aratus(kordus)
ringid = int(input("Mitu ringi: "))
porgandid(ringid)
taringute_arv = int(input("Sisesta täringute arv: "))
taringud(taringute_arv)
taisarv = int(input("Sisesta täisarv: "))
male(taisarv)
mitu_ouna = int(input("Mitu pöialpoissi tahab õuna?: "))
lumivalgeke(mitu_ouna)

