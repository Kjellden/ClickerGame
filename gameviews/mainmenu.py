import arcade
import arcade.gui
from gameviews.gameview import GameView

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class SettingsButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("Settings:", event)
        
class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        
        # get the width and height of the screen
        width, height = self.window.get_size()
        self.window.set_viewport(0, width, 0, height)
        
        self.background = None
        
        # set up gui manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        self.v_box = arcade.gui.UIBoxLayout()
        
        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        setting_button = SettingsButton(text="Settings", width=200)
        self.v_box.add(setting_button.with_space_around(bottom=20))
        
        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)
        
        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start
        
        self.manager.add(
                arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    
    def setup(self):
        self.background = arcade.load_texture("images\Backgroundimg.jfif")
    def on_click_start(self, event):
       game = GameView()
       self.window.show_view(game)
        
    def on_draw(self):
        """
        Render the screen.
        """
        
        self.clear()
        # get screen size so things can scale
        left, screen_width, bottom, screen_height = self.window.get_viewport()
        
        # draw background
        arcade.draw_lrwh_rectangle_textured(0, 0,
            screen_width, screen_height,
            self.background)
        
        # draw button objects in manager
        self.manager.draw()
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P:
            # User hits f. Flip between full and not full screen.
            self.window.set_fullscreen(not self.window.fullscreen)
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)
        
      
