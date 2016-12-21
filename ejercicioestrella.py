import turtle
a=int(input('Igrese el numero de lados de la estrella: '))
t=turtle.Pen()
t.reset()
#impares
n=360/a
m=180+(180/a)
b=(a-2)*(180/n)
for x in range (a):
    t.forward(100)
    t.left(n)
    t.forward(100)
    t.left(m)
turtle.getscreen()._root.mainloop()
