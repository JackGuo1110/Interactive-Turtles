from turtle import Turtle, Screen

class ClickableTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "What do I do?", 
               x = 0 , 
               y = -175):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.window = Screen()

    #set turtle starting states
    self.shape("square")
    self.shapesize(1,3,1)
    self.color("pink")
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)
    self.onclick(self.click)

  # Draws the button name above the button
  def draw_title(self, text, x, y):
    self.goto(self.x, self.y + 17)
    self.write(text, move=False, align='center', font=('Arial', 10, 'normal'))
    self.goto(self.x, self.y)

  # tells what happens when button is clicked
  def click(self, x, y):
    # This is Placeholder:  What should this button do?
    print ("There are two turtles on the map, use wasd to control the first turtle and use the arrow keys to control the second turtle. Try to cath the other turtle without touching the moving objects. Have fun playing tag!")

  # TODO:  
  # 1) Change the button color 
  # 2) make the click method do something else
