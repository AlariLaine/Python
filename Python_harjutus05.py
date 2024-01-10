# Massiivid - Array
# 28.11.23, 5.12.23
# Alari Laine

"""
Vanused
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine

"""

vanused = [13,12,5,16,45,23,34,5,23,98,76]





print(f"Suurim arv on {max(vanused)} ja väikseim arv on {min(vanused)}")           
print(f"Vanuste summa: {sum(vanused)}")
print(f"Keskmine vanus on {round(sum(vanused)/len(vanused), 2)}")

for vanus in vanused:
    print (vanus * "*")


input()



"""
Duplikaadid
Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
Loo kood, mis ei väljasta kordusi.

"""


opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus_opilased = []
for opilane in opilased:
    #kontrolli kas on uues loendis olemas
    if opilane not in uus_opilased:
            #kui pole, siis lisan
            uus_opilased.append(opilane)



print(uus_opilased)

print("")
input()


"""
Nimede lisamine loendisse
Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi lisatud nimi
"""

"""
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
    Õpilased = [Juhan,Kati,Maarja,Mario,Mati]
"""
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
jrk = 1
for opilane in opilased:
    print (f"{jrk}. {opilane}")
    jrk += 1
valik = int(input("mitmendat nime tahad muuta:"))
uusnimi = input("Lisa uus nimi:")
del opilased[valik-1]
opilased.insert(valik-1,uusnimi)


print(opilased)

nimed=[]

for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)
print("viimati lisatud nimi:", nimed[-1])
nimed.sort()
   
   
print(nimed)
