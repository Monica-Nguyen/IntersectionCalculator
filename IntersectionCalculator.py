#Name: Monica Nguyen
#Date: Sept 27, 2019
#The following code shows intersection points (or lack of) for a circle and line drawn by the user using turtle. The program prints how many intersection points there are to the terminal. The bottom left of the screen is (0,0) and the top right is (800,600) in Quadrant 1 of the cartesian coordinate system. Therefore, if the user wants the line and circle to appear in this screen then the inputs must be within the specified parameters.

#Turtle methods used in this program were from https://docs.python.org/3/library/turtle.html#turtle.setposition that were shown in tutorial by Shauvik Shadnan, Computer Science, University of Calgary. 

#Importing the turtle and math library so that we can use the drawing function and do calculations
import turtle
import math

#Constants used for the screen parameters and angle values needed to turn buddy in drawing the axes.
#The math to determine the middle of the window is simple because 800 / 2 = 400 and 600 / 2 = 300, which are the middle of the width and height, respectively. 
WIDTH = 800
HEIGHT = 600
WIDTHHALF = WIDTH/2
HEIGHTHALF = HEIGHT/2
TURNAROUNDDIRECTION = 180 
TURN90DEGREES = 90

#This sets up the "drawing pen" named buddy and sets the screen size to (0,0) as the bottom left corner and (800, 600) being the top right corner. Cite: CPSC231F19A1 document from D2L.
buddy = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0) #0 is the edge of the screen and not a magic number according to what was said in CT Hours
screen.setworldcoordinates(0,0, WIDTH, HEIGHT) #0 is the edge of the screen and not a magic number according to what was said in CT Hours
buddy.hideturtle() #Hiding the cursor as buddy is drawing to give a clearer view of the drawing

#Drawing the black x and y axes in the middle of the screen. 
#The "up()" picks up the pen so that I can start drawing the axes at (0, 300)
#goto() tells buddy to relocate the position
#down() allows for the drawing to happen again
#left() and right () changes the direction in which buddy is facing
#forward() tells buddy how far to draw
#The x and y axes are two straight perpendicular lines. The x axis is drawn then the position is changed to the middle of the x-axis and a 90 degree turn allows the y axis to be drawn perpendicular. The y-axis is made with 300 moving up and then turning to go all the way back down.
buddy.color("black")
buddy.pensize(2)
buddy.speed(7) 
buddy.up()
buddy.goto(0,HEIGHTHALF) #0 is the edge of the screen and not a magic number according to what was said in CT Hours
buddy.down()
buddy.forward(WIDTH)
buddy.left(TURNAROUNDDIRECTION)
buddy.forward(WIDTHHALF)
buddy.right(TURN90DEGREES)
buddy.forward(HEIGHTHALF)
buddy.left(TURNAROUNDDIRECTION)
buddy.forward(HEIGHT)
buddy.up()

#Get user input for the (x,y) coordinates of the position for the circle. #Shifted by r in line 58.
xc = int(input("Enter a positive number for the x-coordinate of the circle: "))
yc = int(input("Enter a positive number for the y-coordinate of the circle: "))
#Get user input for the radius of the circle.
r = float(input("What is the radius of the circle? (Enter a positive number): "))	

#Drawing a red circle from user input
buddy.goto(xc - r,yc) #buddy starts drawing a circle from its starting position. To centre it around the given position from the user, it must be shifted by one radius.
buddy.down()
buddy.color("red")
buddy.circle(r)
buddy.up()

#Get user input for the (x,y) coordinates of the start of the line.
x1 = int(input("Enter a positive number for the x-coordinate of start of the line: "))
y1 = int(input("Enter a positive number for the y-coordinate of start of the line: "))

#Get user input for the (x,y) coordinates of the end of the line.
x2 = int(input("Enter a positive number for the x-coordinate of end of the line: "))
y2 = int(input("Enter a positive number for the y-coordinate of end of the line: "))

#Drawing a blue line from user input
buddy.up()
buddy.color("blue")
buddy.goto(x1,y1)
buddy.down()
buddy.goto(x2,y2)
buddy.up()

#To make the intersection circles and "No Intersect!" green. 
buddy.color("green")

#Variables and constants used for calculations
a = ((x2-x1)**2 + (y2-y1)**2)
b = (2*((x1-xc)*(x2-x1) + (y1-yc)*(y2-y1)))
c = ((x1-xc)**2 + (y1-yc)**2 - r**2)
discriminant = ((b**2) - (4*a*c))
quadraticDenominator = (2*a)
ADJUSTEDX = 365 #This is an adjusted value of x so that "No Intersect!" appears more centered (just for visual appeal)
INTERSECTIONRADIUS = 5 #Radius of the green intersection circle

#This if statement is so that the program does not crash from the square root of a negative number in  math.sqrt(discriminant) prior to the next statements that permit "No Intersect!" and green intersection.
if(discriminant >= 0):
    alpha1 = ((-b) + math.sqrt(discriminant)) / quadraticDenominator
    alpha2 = ((-b) - math.sqrt(discriminant)) / quadraticDenominator 
    intersectx1 = (1 - alpha1)*x1 + alpha1*x2
    intersecty1 = (1 - alpha1)*y1 + alpha1*y2
    intersectx2 = (1 - alpha2)*x1 + alpha2*x2
    intersecty2 = (1 - alpha2)*y1 + alpha2*y2

#When the discriminant of the quadratic formula is negative there cannot be any intersection points. In this case, the turtle screen says "No Intersect!" and the terminal says there are no intersection points.
if discriminant < 0:
    buddy.goto(ADJUSTEDX,HEIGHTHALF)
    buddy.write("No Intersect!") 
    print("There are no intersection points.")

#If the discriminant is zero, then buddy will find the one intersection point and draw a green circle around it. It does not matter which alpha does into here since adding or substracting a 0 is equivalent
elif(discriminant == 0): 
    buddy.goto(intersectx1 - INTERSECTIONRADIUS,intersecty1)
    buddy.down()
    buddy.circle(INTERSECTIONRADIUS)
    print("There is one intersection point.")

#For when discriminant greater than 0, there would be 2 intersection points. One from alpha1 and another from alpha2 because the quadratic formula has an adding and subtracting component. However, both alphas may not be in the line segment.
else: 
    if (alpha1<=1 and alpha1>=0): #When alpha1 is between 1 and 0 inclusive. This is one intersection point. 
        buddy.goto(intersectx1 - INTERSECTIONRADIUS, intersecty1)
        buddy.down() 
        buddy.circle(INTERSECTIONRADIUS) #A radius of 5 for intersection circles
        buddy.up()
        if (alpha2<=1 and alpha2>=0): #When alpha2 falls between 1 and 0 inclusive. This is one intersection point. 
            buddy.goto(intersectx2 - INTERSECTIONRADIUS,intersecty2)
            buddy.down() 
            buddy.circle(INTERSECTIONRADIUS) #A radius of 5 for intersection circles
    
    elif (alpha1>1 or alpha1<0) and (alpha2>1 or alpha2<0): #In the case where alpha1 and alpha 2 are not between 1 and 0, the intersection points  should not be drawn because they fall outside the line segment.
        buddy.goto(ADJUSTEDX,HEIGHTHALF)
        buddy.write("No Intersect!") 
        print("There are zero intersection points.")
    
    else: #To draw only one intersection point originating from either alpha1 or alpha2. When one alpha is between 1 and 0, the other falls outside the range and should not be drawn. 
        if ((alpha1<=1 and alpha1>=0) and (alpha2>1 or alpha2<0)): #When alpha1 is between 1 and 0 where alpha 2 is not.
            buddy.goto(intersectx1 - INTERSECTIONRADIUS, intersecty1)
            buddy.down() 
            buddy.circle(INTERSECTIONRADIUS) #A radius of 5 for intersection circles
            buddy.up()
        else: #When alpha2 is between 1 and 0 where alpha 1 is not. 
            buddy.goto(intersectx2 - INTERSECTIONRADIUS, intersecty2)
            buddy.down() 
            buddy.circle(INTERSECTIONRADIUS) #A radius of 5 for intersection circles
            buddy.up()
     
    #To print only one intersection point originating from either alpha1 or alpha2. When one alpha is between 1 and 0, the other falls outside the range and should not be drawn.      
    if ((alpha1<=1 and alpha1>=0) and (alpha2>1 or alpha2<0)) or ((alpha2<=1 and alpha2>=0) and (alpha1>1 or alpha1<0)):
        print("There is one intersection point.")
   
    if (alpha1<=1 and alpha1>=0) and (alpha2<=1 and alpha2>=0): #When there are two intersection points from both alpha1 and alpha2 being between 1 and 0. 
        print("There are two intersection points.")


#Allows screen to exit when there is a click on the turtle screen
screen.exitonclick()
