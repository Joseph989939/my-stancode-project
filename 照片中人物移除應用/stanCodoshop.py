"""
File: stanCodoshop.py
Name: Joseph
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist_red = (pixel.red - red) ** 2
    dist_green = (pixel.green - green) ** 2
    dist_blue = (pixel.blue - blue) ** 2
    dist = (dist_red + dist_green + dist_blue) ** 0.5
    return float(dist)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    pixels_red_total = 0
    pixels_green_total = 0
    pixels_blue_total = 0
    n = len(pixels)  # total number of elements in a list named pixels
    for i in range(n):
        #  add r, g and b value of all pixels in a list named pixels
        pixels_red_total += pixels[i].red
        pixels_green_total += pixels[i].green
        pixels_blue_total += pixels[i].blue
    # average the sum of r, g and b value of all pixels
    red_avg = int(pixels_red_total / n)
    green_avg = int(pixels_green_total / n)
    blue_avg = int(pixels_blue_total / n)
    rgb = [red_avg, green_avg, blue_avg]
    return rgb  # return a list named rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    red_avg = get_average(pixels)[0]  # the first element (red) of list named rgb
    green_avg = get_average(pixels)[1]
    blue_avg = get_average(pixels)[2]
    n = len(pixels)  # total number of elements (pixel of each picture) in a list named pixels
    nearest_pixel_dist = float('inf')
    nearest_pixel_number = 0
    for i in range(n):  # calculate the distance between pixel rgb value and average rgb value picture by picture
        pixel_dist = get_pixel_dist(pixels[i], red_avg, green_avg, blue_avg)
        # find the pixel which have the nearest distance with average rgb value
        if pixel_dist < nearest_pixel_dist:
            nearest_pixel_dist = pixel_dist
            nearest_pixel_number = i
    return pixels[nearest_pixel_number]  # return the nearest pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    images_numbers = len(images)  # total number of elements (pictures) in a list named images
    for x in range(width):
        for y in range(height):
            pixels = []
            result_pixel = result.get_pixel(x, y)
            for number in range(images_numbers):
                pixels += [images[number].get_pixel(x, y)]  # add pixel (in (x,y)) of each picture into list
            #  fill the r, g, and b values of best pixel to blank image
            result_pixel.red = get_best_pixel(pixels).red
            result_pixel.green = get_best_pixel(pixels).green
            result_pixel.blue = get_best_pixel(pixels).blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
