# Digital Image Processing 
Assignment #1
Due: 10/03/17


 a. (5 pts.) Write code for zooming and shrinking an image using the nearest neighbor and bilinear interpolation. The input to your program is: (i) image, (ii) transformation parameters, and (iii) interpolation method.
 
  - Starter code available in directory resize/      
  - resize/resample.py: One is required to edit the functions "nearest_neighbor" and "bilinear", you are welcome to add more       function. 
  - Do not edit the function "resize"
  - resize/interpolate.py: Write code for linear and bilinear interpolation in there respective function definitions, you are welcome to write new functions and call them from these functions
  - This part of the assignment can be run using dip_hw1_resize.py
  - Usage example: ./dip_hw1_resize.py -i <image-name> -fx <scalex> -fy <scaley> -m <method>
    - image-name: name of the image
    - scalex, scaley: scale to resize the image (eg. fx 0.5, fy 0.5 to make it half the original size)
    - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt


b. (8 pts.) Write a program to binarize a gray-level image based on the assumption that the image has a bimodal histogram.  You are to implement the method to estimate the optimal threshold required to binarize the image. The threshold is to be computed using the average of the expectation of the two distributions. Your code should report both the binarized image and the optimal threshold value. Also assume that foreground objects are darker than background objects in the input gray-level image.

 - Starter code available in directory region_analysis/   
 - region_analysis/binary_image.py:
  - compute_histogram: write your code to compute the histogram in this function, If you return a list it will automatically save the graph in output filder
  - find_optimal_threshold: Write your code to compute the optimal threshold assuming
  - binarize: write your code to threshold the input image to create a binary image here. This function should return a binary image which will automatically be saved in output folder
  
  
c. (7 Pts) Write a program to perform blobcoloring. The input to your code should be a binary image and the output should be a count of total objects in the image as well as the labeled image where each object is color coded starting with the value of 1 and the background taking a value of 0. In addition, your code should also report the area and centroid of each object in the binary image.



