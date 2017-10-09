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

