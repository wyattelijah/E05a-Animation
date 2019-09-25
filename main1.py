"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Mouse Example"
#these 3 lines set the size variables and the title of the game window

class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        # these lines are initializing the class variables as the entered variables
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        # this takes the instance variables and uses them as dimensions and a color for drawing a circle in the game

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # this initializes the game window
        super().__init__(width, height, title)

        # this hides the mouse so only the circle will be seen
        self.set_mouse_visible(False)
        # this sets the background of the window to grey
        arcade.set_background_color(arcade.color.ASH_GREY)

        # this creates and puts the ball in the window
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        # starts the game and draws the circle
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y
        # updates the position of the ball to wherever the mouse is moved
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK
        # turns the ball black when the left mouse button is pressed
    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN
        # turns the ball back to auburn after the left mouse button is released

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
    #runs the game

if __name__ == "__main__":
    main()
    #begins the main function