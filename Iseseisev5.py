# Alari Laine   
# Iseseisev 5

# Korrutamise kontrollimine
import random



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
