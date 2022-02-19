import arcade
from gameviews.mainmenu import MainMenu     


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Clicker Heros"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    menu_view = MainMenu()
    window.show_view(menu_view)
    menu_view.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()