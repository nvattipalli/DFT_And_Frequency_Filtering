import numpy as np


class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        (rows, cols) = image.shape
        for i in range(rows):
            for j in range(cols):
                hist[image[i, j]] += 1
        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0
        c = 0
        ex1 = [0] * 256
        ex2 = [0] * 256
        for i in range(256):
            c += hist[i]
        threshold = c / 2
        for j in range(2):
            for i in range(256):
                if hist[i] < threshold:
                    ex1[j] += ((i + 1) * hist[i]) / c
                if hist[i] >= threshold:
                    ex2[j] += ((i + 1) * hist[i]) / c
            threshold = (ex1[j] + ex2[j]) / 2
            while (ex1[j - 1] - ex1[j]) != 0 and (ex2[j - 1] - ex2[j] != 0):
                j = j + 1
                for i in range(256):
                    if hist[i] < threshold:
                        ex1[j] += ((i + 1) * hist[i]) / c
                    if hist[i] >= threshold:
                        ex2[j] += ((i + 1) * hist[i]) / c
                threshold = (ex1[j] + ex2[j]) / 2
            return threshold



    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        hist = self.compute_histogram(image)
        threshold = self.find_optimal_threshold(hist)

        rows, cols = image.shape
        for i in range(rows):
            for j in range(cols):
                if image[i, j] <= threshold:
                    image[i, j] = 255
                else:
                    image[i, j] = 0
        bin_img = image.copy()
        return bin_img


