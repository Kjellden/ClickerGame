from math import floor
import arcade

class Intern(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(filename= ":resources:onscreen_controls/flat_dark/up.png", scale= .5, center_x= x, center_y= y)
        self.banner_Image = arcade.load_texture("images\\banner.png")
        self.hero = arcade.Sprite(filename= ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", scale= .5, center_x= 50, center_y=y+ 25)
        self.hero_Name = "The intern"
        self.banner_Placement_x = x - x
        self.banner_Placement_y = y - 50
        self._level = 1
        self.base_price = 25
        self.price = 25
        
    def on_draw(self):
        arcade.draw_lrwh_rectangle_textured(self.banner_Placement_x,self.banner_Placement_y,300,100,texture= self.banner_Image)
        self.hero.draw()
        lvl_text = f"{self._level}"
        price = f"Price: {self.price}"
        arcade.draw_text(lvl_text,
                         self.banner_Placement_x + 200,
                         self.banner_Placement_y + 75,
                         arcade.color.BLACK
                         )
        
        arcade.draw_text(price,
                        self.banner_Placement_x + 75,
                         self.banner_Placement_y + 50,
                         arcade.color.BLACK
                         )
        arcade.draw_text(self.hero_Name,
                        self.banner_Placement_x + 75,
                         self.banner_Placement_y + 75,
                         arcade.color.BLACK
                         )
        
    def get_level(self):
        return self._level
    
    def getPrice(self):
        return self.price

    def level_up(self):
        self._level += 1
        self.price = floor((self.base_price + self._level) * (1.10**(self._level-1)))
        
        