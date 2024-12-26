"""
File: babygraphics.py
Name: Joseph
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    years_x_dist = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS)  # count the average distance between years
    x_coordinate = GRAPH_MARGIN_SIZE + years_x_dist * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # create horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # create vertical lines
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # ----- Write your code below this line ----- #
    distance_per_rank = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000  # calculate average distance per rank (y axial)
    name_num = 0
    for name in lookup_names:  # draw lines name to name
        # choose color according name number (name_num)
        name_num += 1
        color_order = (name_num % 4)  # color order (from 1 to 4)
        if name_num % 4 == 0:
            color_order = 4
        # deal with rank
        ranks = []  # list store ranks for y axial (int)
        ranks_text = []  # list store ranks for text (str)
        # find the rank of name year to year, and add into list named ranks
        for year in YEARS:
            if str(year) in name_data[name]:  # find rank (value) by year (key) in dict
                ranks.append(name_data[name][str(year)])
                ranks_text.append(str(name_data[name][str(year)]))
            else:  # rank of name out of 1000 in the year
                ranks.append(1000)
                ranks_text.append('*')
        # draw line by two point (i and i+1)
        for i in range(len(YEARS)-1):
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                               GRAPH_MARGIN_SIZE + int(ranks[i])*distance_per_rank,
                               get_x_coordinate(CANVAS_WIDTH, i+1),
                               GRAPH_MARGIN_SIZE + int(ranks[i+1])*distance_per_rank, fill=COLORS[color_order-1],
                               width=LINE_WIDTH)
        # draw text per year
        for i in range(len(YEARS)):
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                               GRAPH_MARGIN_SIZE + int(ranks[i])*distance_per_rank,
                               text=name + ' ' + ranks_text[i], anchor=tkinter.SW, fill=COLORS[color_order-1])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
