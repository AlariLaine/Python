# Alari Laine
# 10.01.2024
# töö 3


# 1. Konto
fail = open("konto.txt")
for i in fail:
    if float(i) > 0:
        print(i,end="")


# 2. Jukebox
siiamidagi = input("Sisesta faili nimi: ")
fail = open(siiamidagi, encoding="UTF-8")
print("Muusikapalade valik: ")
nr = 1
for i in fail:
    print(f"{nr}. {i}",end="")
    nr+=1
valik = int(input("\n Vali laulu number: "))

fail.seek(0)
nr = 1
for i in fail:
    if nr == valik:
        print(i)
    nr+=1



input()

# tahvli juurde

import datetime
paev = (datetime.datetime.now().day)

fail = open("nimekiri.txt", encoding="UTF-8")
nr = 1
for nimi in fail:
    if nr == paev:
        print(nimi, end="")
    nr+=1
