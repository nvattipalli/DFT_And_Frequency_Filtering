import cv2
import numpy
class cell_counting:


    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        width, height = image.shape
        count = 1
        r = numpy.zeros((width, height), numpy.uint32)
        r1 = numpy.zeros((width, height), numpy.uint32)

        for j in range(height):
            for i in range(width):
                if image[i, j] == 255:
                    if i - 1 >= 0 and j - 1 >= 0:
                        if r[i, j - 1] > 0 and r[i - 1, j] == 0:
                            r[i, j] = r[i, j - 1]
                        if r[i, j - 1] == 0 and r[i - 1, j] > 0:
                            r[i, j] = r[i - 1, j]
                        if r[i, j - 1] == 0 and r[i - 1, j] == 0:
                            r[i, j] = count
                            count = count + 1

                        if r[i, j - 1] > 0 and r[i - 1, j] > 0:
                            r[i, j] = r[i, j - 1]
                            r[i - 1, j] = r[i, j - 1]
                            dec = 2
                            flag = 0
                            while flag == 0:
                                if r[i - dec, j] != 0:
                                    r[i - dec, j] = r[i - dec + 1, j]
                                    dec = dec + 1
                                else:
                                    flag = 1

                    if i == 0 and j > 0:
                        if r[i, j - 1] == 0:
                            r[i, j] = count
                            count = count + 1
                        if r[i, j - 1] > 0:
                            r[i, j] = r[i, j - 1]

                    if j == 0 and i > 0:
                        if r[i - 1, j] > 0:
                            r[i, j] = r[i - 1, j]
                        if r[i - 1, j] == 0:
                            r[i, j] = count
                            count = count + 1


        s = [0] * count
        for i in range(width):
            for j in range(height):
                if r[i, j] > 0:
                    s[r[i, j]] = s[r[i, j]] + 1



        region = {}

        for i in range(width):
            for j in range(height):
                if r[i, j] != 0:
                    if r[i, j] in region:
                        region[r[i, j]].append([i, j])
                    else:
                        region[r[i, j]] = [[i, j]]
        computeStats = {}
        count = 1
        for a in region.keys():

            flag = 0
            for ec in region[a]:
                if (flag == 0):
                    fx = ec[0]
                    fx2 = ec[0]
                    fy = ec[1]
                    fy2 = ec[1]
                    flag = 1
                else:
                    if (fx > ec[0]):
                        fx = ec[0]
                    elif (fx2 < ec[0]):
                        fx2 = ec[0]
                    if (fy > ec[1]):
                        fy = ec[1]
                    elif (fy2 < ec[1]):
                        fy2 = ec[1]

            dif1 = fx2 - fx
            avg1 = dif1 / 2
            centX = fx + avg1
            dif2 = fy2 - fy
            avg2 = dif2 / 2
            centY = fy + avg2
            count = count + 1
            computeStats[count] = [len(region[a]), [centX, centY]]

            for i in range(width):
                for j in range(height):
                    if s[r[i, j]] > 15:
                        r1[i, j] = r[i, j]
                        if r1[i, j] == 0:
                            r1[i, j] = 0
                        else:
                            r1[i, j] = 255


        print(computeStats)

        return r1, computeStats

    def compute_statistics(self, regions):
        return regions[1]

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        for a in stats.keys():
            cv2.putText(image, '*' + repr(a) + ',' + repr(stats[a][0]), (int(stats[a][1][1]), int(stats[a][1][0])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.25, 100)

        return image