#Alari Laine 9.11.23
#ylesanne 2 TURTLE

import turtle

w = turtle.Screen()
w.setup(300,300)
w.title("A.Laine Ylesanne 02")

kaugus = 100
nurk = 60
nurkadearv = 3
kolmnurk = 3
kolmnurknurk = 120
#loome kilpkonna

def viisknurk():
    john = turtle.Turtle()
    for i in range(nurkadearv):
        print(i)
        john.fd(kaugus)
        john.rt(nurk)

def teeKolmnurk(n, k, kn):
    john2 = turtle.Turtle()
    john2.color("red")
    for j in range(n):
        print(j)
        john2.fd(-k)
        john2.rt(kn)
        
teeKolmnurk(3, 50, 120)


turtle.exitonclick()