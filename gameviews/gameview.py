import arcade
from scripts.intern import Intern
from scripts.banker import Banker
from scripts.taxfraud import Taxfraud
from scripts.coin import Coin

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("images\Backgroundimg.jfif")
        self.intern = Intern(x=200, y=400)
        self.banker = Banker(x=200, y=300 )
        self.taxfraud = Taxfraud(x=200, y= 200)
        self.coin = Coin(x=600, y= 300)
        # get the width and height of the screen
        width, height = self.window.get_size()
        self.window.set_viewport(0, width, 0, height)
        self.gold = 0
        self.hit_coin = arcade.load_sound(':resources:sounds/rockHit2.wav')
        self.upgrade_hero = arcade.load_sound(':resources:sounds/upgrade4.wav')
    
    def on_draw(self):
        self.clear()
        # get screen size so things can scale
        left, screen_width, bottom, screen_height = self.window.get_viewport()
        arcade.draw_lrwh_rectangle_textured(0, 0,
            screen_width, screen_height,
            self.background)
        
        arcade.draw_text(f"Gold: {self.gold:.0f}",
                        400,
                        550,
                         arcade.color.BLACK,font_size=25
                         )
        
        self.intern.on_draw()
        self.intern.draw()
        self.banker.on_draw()
        self.banker.draw()
        self.taxfraud.on_draw()
        self.taxfraud.draw()
        self.coin.draw()
        
    def on_update(self, delta_time: float):
        self.gold += self.banker.get_gpm() * delta_time
        self.gold += self.taxfraud.get_gpm() * delta_time
        
        
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        point = (x,y)
      
        if self.coin.collides_with_point(point):
            self.gold += self.intern.get_level() 
            arcade.play_sound(self.hit_coin)
            
        if self.intern.collides_with_point(point):
            if self.gold >= self.intern.price:
                self.gold -= self.intern.price
                arcade.play_sound(self.upgrade_hero)
                self.intern.level_up()
                
        if self.banker.collides_with_point(point):
            if self.gold >= self.banker.price:
                self.gold -= self.banker.price
                arcade.play_sound(self.upgrade_hero)
                self.banker.level_up()
                
        if self.taxfraud.collides_with_point(point):
            if self.gold >= self.taxfraud.price:
                self.gold -= self.taxfraud.price
                arcade.play_sound(self.upgrade_hero)
                self.taxfraud.level_up()
        