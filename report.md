1. Resampling
I have used only the resample.py file for writing the logics for both Nearest Neighbor and Bilinear Interpolation. For finding out Bilinear interpolation, I had to find the linear interpolation thrice which I did it in bilinear_interpolation function itself and hence did not use interpolation.py file.
a) Nearest Neighbor
For Nearest Neighbor, 
* I have created a new image with the size equal to the existing image multiplied by the scaling factor.
* To find out the pixel values of the new image, I have divided the position of each image with the scaling factor to find out the corresponding value in the existing image using
newimage_nearest[i, j] = image[int(i / fx), int(j / fy)]

* Returned the new image.

b) Bilinear
For Bilinear interpolation,
* I have created a new image with the size equal to the existing image multiplied by the scaling factor.
* I have found out the intensities of all the four neighbors for each point i.e., (x_coordinate, y_coordinate) intensities is found out by finding the intensity values of (x, y), (x+1,y) and (x, y+1), (x+1, y+1)  and then finding out the intensity of these two data sets again using the Linear Interpolation formula 
I = I1(x2 - x)/(x2 – x1) + I2(x – x1)/(x2 – x1)

* Since I have calculated the Linear Interpolation in bilinear_interpolation function itself, I have not used the interpolation.py file.

2. binary_image
a)There are three subtasks here – computing histogram, finding optimal threshold and then binarizing the image
i) To compute the histogram I have found out the frequency of each pixel value between 0 and 255

ii) finding optimal threshold
I have taken the threshold value as the middle value of intensity which is equal to 127 and divided the entire range into two parts. For the first set, I have calculated the expected mean value and followed the same steps to find out the expected mean of the second set.
I have taken the average of mean1 and mean2 which is the new threshold.
I then calculated the change in threshold and then followed the above steps till the change in threshold reaches to zero which is the optimal threshold

iii) binarizing the image
Based on the optimal threshold value, I have set the pixel values of all the pixels greater than the threshold value to zero and rest of the pixel values to 255

b) Blob coloring
I have used the blob coloring algorithm mentioned in your slides and found out the regions by scanning the image left to right and top to bottom. Since the first row and the first column do not have the adjacent pixels, I have written a special case to handle them. I have created a dictionary to store the list of regions and returned those values to compute the statistics.

c) I have computed the statistics which includes the region number, area and centroid of each region whose area is greater than 15. I have returned an image which prints all the required statistics. 



