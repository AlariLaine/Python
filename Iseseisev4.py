# Iseseisev töö 4
# Alari Laine
# 10.01.2024

#tervitus

kylalised = 3
def tervitus(n):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {n}. kord tervitada!")
    print('Külaline: "Tere, suur tänu kutsumast!"')

for i in range(kylalised):
    tervitus(i+1)


input()
#eelarve

def eelarve(kylalised):
    summa = kylalised*10+55
    return summa

palju = int(input("Külaliste arv: "))
palju2 = int(input("Mitu tuleb: "))
print(f"Maksimaalne eelarve: {eelarve(palju)}€")
print(f"Minimaalne eelarve: {eelarve(palju2)}€")

input()
# mahl

def mahlapakkidearv(kg):
    pakid = round(kg * 0.4 /3)
    return pakid

kogus = float(input("Õunte kogus: "))
print(mahlapakkidearv(kogus))



#------------------------------------------------------------
def banner(t):
    print(t.upper())

ask = int(input("Mitu korda: "))
ask2 = input("Reklaamlause: ")

for i in range(ask):
    banner(ask2)