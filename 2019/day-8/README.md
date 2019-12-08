# [Day 8](./src)

### [Part one](./src/part_1.py)

Compared to the previous days this one was very straight-forward. We are given a string of numbers between 0 and 2. We are also given a Width and a height of our image. We can decode the string into layers of our image, where each pixel of the image is represented by an input number. There are several layers, which is to say the input is a multiple of the width * height of the image. The first part was to get the layer with the least number of 0 character pixels. The solution I took was to iterate over each section of the input where each section is of length width * height. Then to count the number of zeroes, if it is less than the current minimum conut we replace and and move on. Then we output the solution by multiplying the number of ones by the number of twos in the found layer.

Runtime: 0.01s

### [Part two](./src/part_2.py)

Runtime: 0.01s

Here we expanding on the concept of layers a bit more. Each pixel as stated previously, has one of 3 states. 0 means it is a black pixel, 1 is a white piel, and 2 is a trasparent pixel. The layers are stacked below one another, which is to say the first layer is on top, the second is below the first, etc.... Then each pixel is defined by combining the layers top to bottom. If the pixel at the first layer is 2 it is transparent, so the colour we see will be on one of the lower layers, we continue this until we hit a non-transparent pixel. This will be the pixel we see, either a black pixel or a white pixel.

The approach I took was to initalize a fully transparent layer that sits on top of everything. Then we get each layer and iterate through each pixel in each layer. If the pixel in the previous layer is two and the pixel in the current layer is not 2 we replace it with the pixel in the current layer. We continue this until we have gone through each layer. 

The fun part here was that an actual message was printed out. I had to replace the zeroes with blank spaces so I could read the message more easily. Then I printed the image line by line, so printing each row of 25 pixels at a time, then reading it we get our solution!
