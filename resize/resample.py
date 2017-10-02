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
        (rows, cols) = image.shape
        fx = float(fx)
        fy = float(fy)

        newimage = np.ones((int(fx * rows), int(fy * cols)), np.uint8) * 255

        for i in range(int(rows * fx)):
            for j in range(int(cols * fy)):
                newimage[i, j] = image[int(i / fx), int(j / fy)]

        image = newimage

        return image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        (rows, columns) = image.shape
        fx = float(fx)
        fy = float(fy)
        bilinear_interpolation_image = np.ones((int(fx * rows), int(fy * columns)), np.uint8) * 255
        for i in range(int(rows * fx)):
            for j in range(int(columns * fy)):
                x_coordinate = i / fx
                y_coordinate = j / fy
                x = (math.floor(x_coordinate))
                y = (math.floor(y_coordinate))
                if ((x + 1) > rows - 1):
                    x = rows - 2
                if ((y + 1) > columns - 1):
                    y = columns - 2
                intensity1 = (x + 1 - int(x_coordinate)) * image[x + 1, y] + (int(x_coordinate) - x) * image[x, y]
                intensity2 = (x + 1 - int(x_coordinate)) * image[x + 1, y + 1] + (int(x_coordinate) - x) * image[
                    x, y + 1]
                bilinear_interpolation_image[i, j] = (y + 1 - int(y_coordinate)) * intensity2 + (int(
                    y_coordinate) - y) * intensity1
        image = bilinear_interpolation_image

        return image