import turtle

w=turtle.Screen()
w.bgcolor("indigo")
sc=turtle.Turtle()

sc.color("yellow")
def sqrfunc(size):
    for i in range(4):
        sc.fd(size)
        sc.left(90)
        size=size+10

i=6
for j in range(20):
    i+=40
    sqrfunc(i)