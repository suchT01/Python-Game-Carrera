import turtle
import random
s=turtle.Screen()
s.title("Primer Proyecto")

j1=turtle.Turtle()
j2=turtle.Turtle()
j1.hideturtle()
j2.hideturtle()

j1.shape("turtle")
j1.color("green","blue")
j1.shapesize(2,2,2)
j1.pensize(3)

j2.shape("turtle")
j2.color("orange","red")
j2.shapesize(2,2,2)
j2.pensize(3)

j1.penup()
j1.goto(200,100)
j1.pendown()
j1.circle(30)
j1.penup()
j1.goto(-200,130)
j1.showturtle()

j2.penup()
j2.goto(200,-100)
j2.pendown()
j2.circle(30)
j2.penup()
j2.goto(-200,-70)
j2.showturtle()

dado=[1,2,3,4,5,6]

for i in range(20):
    if j1.pos() >= (185,130):
        print("El jugador 1 ha ganado.")
        break
    elif j2.pos() >= (185,-70):
        print("El jugador 2 ha ganado")
        break
    else:
        turno1=input("Presione la tecla enter para avanzar el j1.")
        turno1=random.choice(dado)
        print("Tu numero es: ",turno1," y Avanzas: ",turno1*20)
        j1.pendown()
        j1.forward(turno1*20)

        turno2=input("Presione la tecla enter para avanzar el j2.")
        turno2=random.choice(dado)
        print("Tu numero es: ",turno2," y Avanzas: ",turno2*20)
        j2.pendown()
        j2.forward(turno2*20)


turtle.done()