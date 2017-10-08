import cv2
import math
import numpy as np
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

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        (width, height) = image.shape
        fx = float(fx)
        fy = float(fy)

        newimage_nearest = np.ones((int(fx * width), int(fy * height)), np.uint8) * 255

        for i in range(int(width * fx)):
            for j in range(int(height * fy)):
                newimage_nearest[i, j] = image[int(i / fx), int(j / fy)]

        image = newimage_nearest

        return image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        (width, height) = image.shape
        fx = float(fx)
        fy = float(fy)
        newimage_bilinear = np.zeros((int(fx * width), int(fy * height)), np.uint8) * 255
        for i in range(int(width * fx)):
            for j in range(int(height * fy)):
                x_coordinate = i / fx
                y_coordinate = j / fy
                x = (math.floor(x_coordinate))
                y = (math.floor(y_coordinate))
                if ((x + 1) > width - 1):
                    x = width - 2
                if ((y + 1) > height - 1):
                    y = height - 2
                intensity1 = image[x, y] * (((x + 1) - int(x_coordinate)) / ((x + 1) - x)) + image[x + 1, y] * (
                    (int(x_coordinate) - x) / ((x + 1) - x))
                intensity2 = image[x, y + 1] * (((x + 1) - int(x_coordinate)) / ((x + 1) - x)) + image[x + 1, y + 1] * (
                (int(x_coordinate) - x) / ((x + 1) - x))
                newimage_bilinear[i, j] = (((y + 1) - int(y_coordinate)) / ((y + 1) - y)) * intensity1 + ((int(
                    y_coordinate) - y) / ((y + 1) - y)) * intensity2
        image = newimage_bilinear

        return image