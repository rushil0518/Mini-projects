import turtle
import time
import random
print("WELCOME to the turtle race") 
num = int(input("Enter the number of turtles for the race (2-10) : "))
if (num < 2 or num > 10) :
    print ("Please enter a valid number of turtles")


WIDTH,HEIGHT = 500,500
COLORS = ["red","blue","cyan","black","pink","orange","brown","green","purple","yellow"]
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Turtle race")


random.shuffle(COLORS)
colors = COLORS[:num]

def race(colors) :
    turtles = create_racers(colors)

    while True :
      for racers in turtles :
         distance =  random.randrange(1,20)
         racers.forward(distance)
         x,y = racers.pos()
         if (y >= HEIGHT//2 - 10) :
               return colors[turtles.index(racers)]
               


def create_racers (colors) :
    turtles = []
    spacing = WIDTH//(len(colors)+1)
    for i,color in enumerate(colors) :
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.left(90)
        racer.setpos(-WIDTH//2 + (i+1)*spacing , -HEIGHT//2 + 20)
        turtles.append(racer)
        racer.pendown()

    return turtles

winner = race(colors)
print(f"{winner} is the winner")

time.sleep(5)