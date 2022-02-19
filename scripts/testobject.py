import arcade
class buttonObject(arcade.Sprite):
    def __init__(self):
        super().__init__(filename= ":resources:onscreen_controls/flat_dark/up.png", scale= .5, center_x= 200, center_y= 150)
        self.score = 0
        self.banner = arcade.load_texture("images\\banner.png")
        self.hero_Image = arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")
        
        
    def on_draw(self):
        output = f"score = {self.score}"
        arcade.draw_text(output,
                         100,
                         50,
                         arcade.color.BLACK,
                         )
        arcade.draw_lrwh_rectangle_textured(0,100,300,100,self.banner)
        self.hero_Image.draw_sized(100,100, 50, 50)
    def add_score(self):
        self.score += 1