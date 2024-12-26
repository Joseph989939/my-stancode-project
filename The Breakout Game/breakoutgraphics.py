"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Build a constructor that can creates all objects of breakout game.
For example,window of the game, bricks with colors, black ball, black paddle, and the initial speed of black ball.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks 橫列
BRICK_COLS = 10       # Number of columns of bricks 直行
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 4    # Initial vertical speed for the ball
MAX_X_SPEED = 2        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=self.window_width/2-paddle_width/2, y=self.window_height-paddle_offset)
        self.pdw = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(width=2*ball_radius, height=2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=self.window_width//2-ball_radius, y=self.window_height//2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        self.total_bricks = 0
        for i in range(brick_rows):  # the number of rows
            for j in range(brick_cols):  # the number of columns
                brick_i_j = GRect(width=brick_width, height=brick_height)
                brick_i_j.filled = True
                # fill brick with colors
                if (i+1) % 12 == 1 or (i+1) % 12 == 2:
                    brick_i_j.fill_color = 'red'
                elif (i+1) % 12 == 3 or (i+1) % 12 == 4:
                    brick_i_j.fill_color = 'orange'
                elif (i+1) % 12 == 5 or (i+1) % 12 == 6:
                    brick_i_j.fill_color = 'yellow'
                elif (i+1) % 12 == 7 or (i+1) % 12 == 8:
                    brick_i_j.fill_color = 'green'
                elif (i+1) % 12 == 9 or (i+1) % 12 == 10:
                    brick_i_j.fill_color = 'blue'
                elif (i+1) % 12 == 11 or (i+1) % 12 == 12:
                    brick_i_j.fill_color = 'purple'
                self.window.add(brick_i_j, x=(brick_width+brick_spacing)*j,
                                y=brick_offset+(brick_height+brick_spacing)*i)
                self.total_bricks += 1  # use to calculate total number of bricks

        # use to run function ball_move while click the mouse firstly
        self.check = True

    # on mouseclick function
    def paddle_move(self, event):
        if event.x < self.pdw/2:
            self.paddle.x = 0
        elif event.x > self.window_width - self.pdw/2:
            self.paddle.x = self.window_width - self.pdw
        else:
            self.paddle.x = event.x - self.pdw / 2

    # get initial velocity of ball while click firstly
    def ball_move(self, event):
        if self.check:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random()) > 0.5:
                self.__dx = -self.__dx
            self.check = False  # will not change initial velocity no matter any mouseclick

    def get_vx(self):  # getter function for user to get initial velocity (x axial)
        vx = self.__dx
        return vx

    def set_vx(self):  # setter function for user to set rebound velocity (x axial)
        self.__dx = -self.__dx

    def set_vx_stop(self):  # setter function for user to set velocity = 0 (x axial)
        self.__dx = 0

    # velocity (y axial)
    def get_vy(self):
        vy = self.__dy
        return vy

    def set_vy(self):
        self.__dy = -self.__dy

    def set_vy_stop(self):
        self.__dy = 0

    # check ball touch brick or paddle, and rebound
    def detect_obj(self):
        # four corner location of ball
        for detect_x in range(self.ball.x, self.ball.x + self.ball.width+1, self.ball.width):
            for detect_y in range(self.ball.y, self.ball.y + self.ball.height+1, self.ball.height):
                obj = self.window.get_object_at(detect_x, detect_y)  # object that ball touched
                if obj:  # obj is True
                    if obj is self.paddle:
                        self.set_vy()
                        return
                    else:  # object is brick
                        self.window.remove(obj)
                        self.set_vy()
                        self.total_bricks -= 1
                        return

    # when ball fall out of bottom of window, return ball to original position
    def restart(self):
        self.ball.x = self.window.width // 2 - self.ball.width // 2
        self.ball.y = self.window.height // 2 - self.ball.height // 2
        self.check = True  # makes on mouseclick function work successfully

