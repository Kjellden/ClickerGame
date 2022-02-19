import arcade

class Coin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(filename= ":resources:images/items/gold_1.png", scale= 3, center_x= x, center_y= y)