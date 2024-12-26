"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Use constructor to create the animation of breakout game (include ball rebound, paddle move with mouse,
and broke bricks when ball touch the bricks)
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES
    while num_lives > 0 or graphics.total_bricks > 0:  # stop condition
        pause(FRAME_RATE)
        if not graphics.check:  # when graphics.check is False, run
            if num_lives > 0 and graphics.total_bricks > 0:
                graphics.ball.move(graphics.get_vx(), graphics.get_vy())
                # ball rebound from window (x axial)
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_vx()
                # ball rebound from window (y axial)
                if graphics.ball.y <= 0:
                    graphics.set_vy()
                graphics.detect_obj()  # detect object function
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    num_lives -= 1  # when ball fall out of window
                    graphics.restart()  # ball return


if __name__ == '__main__':
    main()
