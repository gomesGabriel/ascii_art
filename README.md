# ascii_art
The project was developed for the ASCII art challenge proposed by R U Hacking.
For development uses a python language to develop code that reads and converts the image to ASCII

When converting an image to ASCII text it is necessary to follow a few steps:
 - Resize the image to the custom size keeping an aspect ratio
 - Convert the image to grayscale
 - Convert each gray pixel to an ASCII character that has the same intensity as the pixel

To build the code that converts an image into ASCII text, it uses the PIL library that reads the image
```
import PIL.Image
```
Our development consisted of creating functions that make each part of the step

A resize function:
```
resize_image ()
```

One to make the image grayscale
```
greyfy()
```

Another to convert each pixel to an ASCII character
```
pixels_to_ascii()
```

And also a *main* function where the inputs and function calls are.

The code receives only the image path and returns both a txt file containing the converted image and the text in the terminal itself.


An exemple of ASCII art is (we recommend copying and pasting the following characters into a text editor):
![Alt text](https://github.com/gomesGabriel/ascii_art/blob/main/g_ascii.jpg)

Base image for prior art:
![Alt text](https://github.com/gomesGabriel/ascii_art/blob/main/g.jpg)
