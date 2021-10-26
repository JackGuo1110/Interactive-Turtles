from turtle import Turtle, ontimer


class MovingTurtle(Turtle):
  def __init__(self, width, player1, player2):
    Turtle.__init__(self)
    self.width = width
    self.player1 = player1
    self.player2 = player2

    # initial setup
    self.shape("square") 
    self.color("purple")
    self.shapesize(.5, .5, 1)
    self.penup()
    self.collision_distance = 20

    self.shape("square") 
    self.color("blue")
    self.shapesize(.5, .5, 1)
    self.penup()
    ontimer(self.move_self,2)
    self.collision_distance = 20
    

    # variables
    self.x_spd = 4
    
  def move_self(self):
    self.forward(self.x_spd)
    if self.at_edge():
      self.x_spd = -self.x_spd
    if self.check_collision(self.player1):
      print("CRASH! You lose")
      quit()
    if self.check_collision(self.player2):
      print("CRASH! You lose")
      quit()
    ontimer(self.move_self,2)

  def at_edge(self):
    if self.xcor() >= self.width/2 or self.xcor() <= -self.width/2:
      return True
    else:
      return False

  def hit_ball(self):
     if self.check_collision(self.player1, self.player2):
      print("You hit the obstacle, try again!")
      quit()


  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False
