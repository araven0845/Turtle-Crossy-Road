import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
game_is_on = True
screen.listen()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, "Up")
    cars.create_car()
    cars.drive()
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.level_up()
        cars.speed_up()
        scoreboard.increase_score()





screen.exitonclick()