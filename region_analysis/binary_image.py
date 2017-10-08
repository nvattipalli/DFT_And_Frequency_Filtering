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

        maxIntensity = len(hist) - 1
        threshold = int(maxIntensity / 2)
        changeInThreshold = maxIntensity
        while True:
            if (changeInThreshold < 1):
                break
            sum1 = 0
            mean1 = 0
            for i in range(0, threshold):
                sum1 = sum1 + hist[i]

            for i in range(0, threshold):
                mean1 = mean1 + (i + 1) * (hist[i] / sum1)


            sum2 = 0
            mean2 = 0
            for i in range(threshold, maxIntensity - 1):
                sum2 = sum2 + hist[i]

            for i in range(threshold, maxIntensity - 1):
                mean2 = mean2 + (i + 1) * (hist[i] / sum2)

            newThreshold = int((mean1 + mean2) / 2)
            changeInThreshold = newThreshold - threshold
            threshold = newThreshold
        return threshold


    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        bin_img = image.copy()
        hist = self.compute_histogram(bin_img)
        threshold = self.find_optimal_threshold(hist)
        (row, col) = image.shape
        # hist = [0] * 256

        for i in range(0, row):
            for j in range(0, col):
                if (image[i][j] < threshold):
                    bin_img[i][j] = 255
                else:
                    bin_img[i][j] = 0

        return bin_img