"""dip_hw1.py: Starter file to run howework 1"""

#Example Usage:

__author__      = "Pranav Mantini"
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"

import cv2
import sys

def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-r", "--resample", dest="resample",
                        help="specify the name of the image and scale size", metavar="RESAMPLE IMAGE")
    parser.add_argument("-c", "--regioncount", dest="regioncount",
                        help="specify the image for regioncounting", metavar="COUNT REGIONS")

    args = parser.parse_args()

    if args.resample is None:
        print("Please specify the name of image to resize and size")
        print("use the -h option to see usage information")
        sys.exit(2)

    else




if __name__ == "__main__":
    main()







