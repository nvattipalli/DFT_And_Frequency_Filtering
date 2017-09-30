import cv2
import math
import numpy as np
from math import floor
from dip_hw1_region_analysis import display_image
from matplotlib import pyplot as plt
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    img = cv2.imread('result.png', 0)

    def nearest_neighbor(self, image, fx, fy):
        (rows, cols) = image.shape
        nrow = round(rows * fx)
        ncol = round(cols * fy)

        temp = np.zeros((nrow, ncol))

        for i in range(nrow):
            for j in range(ncol):
                temp[i, j] = image[floor(i / fx), floor(j / fy)]

        image = temp
        return image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        return image

