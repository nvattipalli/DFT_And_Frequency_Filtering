# Digital Image Processing 
Assignment #1
Due: 10/03/17

1. Resampling:
(5 pts.) Write code for zooming and shrinking an image using the nearest neighbor and bilinear interpolation. The input to your program is: (i) image, (ii) transformation parameters, and (iii) interpolation method.
 
  - Starter code available in directory resize/      
  - resize/resample.py: One is required to edit the functions "nearest_neighbor" and "bilinear", you are welcome to add more       function. 
  - Do not edit the function "resize"
  - resize/interpolate.py: Write code for linear and bilinear interpolation in there respective function definitions, you are welcome to write new functions and call them from these functions
  - This part of the assignment can be run using dip_hw1_resize.py
  - Usage example: ./dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method
    - image-name: name of the image
    - scalex, scaley: scale to resize the image (eg. fx 0.5, fy 0.5 to make it half the original size)
    - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt

2. Region Counting:
 a. (8 pts.) Write a program to binarize a gray-level image based on the assumption that the image has a bimodal histogram.  You are to implement the method to estimate the optimal threshold required to binarize the image. The threshold is to be computed using the average of the expectation of the two distributions. Your code should report both the binarized image and the optimal threshold value. Also assume that foreground objects are darker than background objects in the input gray-level image.
 - Starter code available in directory region_analysis/   
 - region_analysis/binary_image.py:
  - compute_histogram: write your code to compute the histogram in this function, If you return a list it will automatically save the graph in output filder
  - find_optimal_threshold: Write your code to compute the optimal threshold assuming
  - binarize: write your code to threshold the input image to create a binary image here. This function should return a binary image which will automatically be saved in output folder  
  
 b. (7 Pts) Write a program to perform blobcoloring. The input to your code should be a binary image and the output should be a list of objects or regions in the image. 
 - region_analysis/cell_counting.py:
  - blob_coloring: write your code for blob coloring here, takes as input a binary image and returns a list of objects or regions.
  
 c. (5 Pts) Ignore cells smaller than 15 pixels in area and generate a report of the remaining cells (Cell Number, Area, Location). 
  - compute_statistics: write your code for computing the statistics of each object/region, i.e area and location(centroid) here.
  Print out the statistics to stdout. region number, area and centroid for each region. 
  - mark_regions_image: write your code to create a final cell labeled image. The final image should include an astrix representing the centroid of each cell and two numbers, one representing its Cell Number and another its area. Please see sample output below.\
  
  ![Alt text](results.png?raw=true "Sample output")
  
  
  - Usage example: ./dip_hw1_region_analysis.py -i image-name
    - image-name: name of the image    
  - Please make sure your code runs when you run the above command from prompt
  
Two images are provided for testing: cells.png and cell2.jpg


  
PS. Files not to be changed: requirements.txt and .circleci directory
If you do not like the structure, you are welcome to change the over all code. 
However under two stipulations:
1. the first part has to run using command
 ./dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method
  and the second part using
  ./dip_hw1_region_analysis.py -i image-name  
2. Any output file or image should be written to output/ folder

The TA will only be able to see your results if these two conditions are met




  

 



