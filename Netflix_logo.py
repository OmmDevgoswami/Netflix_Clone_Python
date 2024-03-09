def logo_leg(colour, bre , leng):
    if colour == "":
        colour = "black"
    for i in range(2):
        turt.begin_fill()
        turt.fillcolor(colour)
        turt.forward(bre)
        turt.right(90)
        turt.forward(leng)
        turt.right(90)
        turt.end_fill()
        
def turt_move(x,y):
    turt.up()
    turt.goto(x,y)
    turt.down()

import turtle
turt = turtle.Turtle()
bg = turtle.Screen()
turt.hideturtle()
bg.bgpic("C:\\Users\\teamu\\Dropbox\\PC\\Desktop\\py codes\\netflix background.gif")
turt.color("#D81F26")
turt.speed(6)

#First_Leg
turt_move(-70,100)
logo_leg("#E50914",30,130)

#N
turt_move(-70,81)
turt.setheading(35)
logo_leg("#E50914" ,35,135)
        
#End_Leg
turt_move(38,-30)
turt.setheading(180)
logo_leg("#E50914",30,130)

turt.speed(3)
turt_move(-78,-80)
turt.write("NETFLIX", font = ("Consolas",24,"bold"))

#Log_In
turt.speed(0)
turt_move(-135,-120)
turt.color("White")
turt.setheading(90)
logo_leg("",25,250)
turt_move(-130,-121)
turt.write("Email Or Phone Number", font = (2))

turt_move(-135,-160)
logo_leg("",25,250)
turt_move(-130,-161)
turt.write("Password", font = (2))

turt_move(-130,-190)
turt.write("<- Need help?", font=("bold",10))

turt_move(-130,-210)
turt.write("New to Netflix? Sign up now.", font=("bold",10))

turt_move(45,-200)
turt.color("#E50914")
logo_leg("#E50914",35,70)
turt.color("White")
turt_move(48,-195)
turt.write("Sign in", font = ("bold",16))

print("Done")

turtle.done()
