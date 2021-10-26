from turtle import Screen
from keyboard import KeyboardTurtle
from clickableturtle import ClickableTurtle
from movingturtle import MovingTurtle
#from keyboard2 import KeyboardTurtle2
from Wall import wall


# set up instance ofw the screen
window = Screen()
window.bgpic("l.png")

screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance
button = ClickableTurtle()

wall_list = []

#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)

player_2 = KeyboardTurtle(window, "w", "s","d","a")
player_1.goto(200, 100)
player_2.goto(-100, -80)





w1 = wall(100, 0, 1, 5)
wall_list.append(w1)
wall_list.append(wall(0, 100, 5, 1))


# set target of other player(our collison check) to the opposite player
player_1.other_player = player_2
player_2.other_player = player_1


moveT = MovingTurtle(screen_width, player_1, player_2)
moveT.other_player = player_2 and player_1
moveT.goto(10,10)

# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment