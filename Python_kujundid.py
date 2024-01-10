# Alari Laine
# 28.11.23
# Hinne

import random
import turtle

"""
Turtle (if, for), Python 5- (6. - 9. Tund) /
Hinne: Kilpkonn (IF, FOR)
- funktsioon, mis loob erineva suuruse ja asukohaga viisnurga kogu platsi ulatuses (üle ääre ei tohi minna)
- funktsioon, mis loob erineva suuruse ja asukohaga kolmnurki kogu platsi ulatuses
- funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt viisnurki ja kolmnurki
- menüü -> küsib kasutajalt, millist kujundit soovib, küsib kogust ja kui ära joonistab, siis küsib jälle. EXIT võimalus.
"""

w = turtle.Screen()
w.setup(600,600)


def looViisnurk():
    a = random.randint(10,200)
    x = random.randint(-300,300-a)
    y = random.randint(-300+(a//2),300-(a//2))
    john = turtle.Turtle()
    R = random.random()
    G = random.random()
    B = random.random()
    
    john.color(R, G, B)
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.lt(random.randint(0,360))
    for i in range(5):
        john.fd(a)
        john.rt(144)
    
def looKolmnurk():
    
    a = random.randint(10,100)
    x = random.randint(-300,300-a)
    y = random.randint(-300+(a//2),300-(a//2))
    john = turtle.Turtle()
    R = random.random()
    G = random.random()
    B = random.random()
    
    john.color(R, G, B)
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.lt(random.randint(0,360))
    for i in range(3):
        john.fd(a)
        john.rt(120)
        
def looSuvaline():
    suv = random.randint(1,2)
    print(suv)
    if suv == 1:
        looViisnurk()
    else:
        looKolmnurk()
        
def kuvaMenyy():
    loop = 1
    while loop == 1:
        valikujund = w.numinput("Kujundi valik","1. Vali viisnurk \n2. Vali kolmnurk \n3. Vali suvaline \n4. VÄLJU")
        if valikujund >= 4:
            exit()
        valikogus = int(w.numinput("Kujundite arv","Vali kujundite arv:"))
        for i in range (valikogus):
            if valikujund == 1:
                looViisnurk()
            elif valikujund == 2:
                looKolmnurk()
            elif valikujund == 3:
                looSuvaline()
            else:
                print("EXIT")

kuvaMenyy()

turtle.exitonclick()
