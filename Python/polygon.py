import turtle, math

# 4.12 Exercises to be done

# Drawing a square
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

length = int(input('How big should polygon be? '))
sides = int(input('How many sides should polygon be? '))
bob = turtle.Turtle()
polygon(bob, length, sides)

def circle(t, r):
    circumference = 2*math.pi*r
    n = int(circumference/3)+3
    length = circumference / n
    polygon(t, length, n)
