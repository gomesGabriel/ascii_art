from os import path
import PIL.Image
import sys
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
ASCII_CHAR_TRANSPARENT = '.'

def resize_image(image, new_width=100):
    width, heigth = image.size
    ratio = heigth/width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, int(new_height/2)))
    #resized_image = image.resize((new_width, int(new_height/3 * 2)))
    #resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayfy(image):
    grayscale_image = image.convert("LA")
    return(grayscale_image)

def pixels_to_ascii(image):
    gray_pixels = image.getdata(0)
    alpha_pixels = image.getdata(1)
    pixel_count = len(gray_pixels)
    characters = "".join([(ASCII_CHAR_TRANSPARENT if alpha_pixels[i] == 0 else ASCII_CHARS[gray_pixels[i]//25]) for i in range(pixel_count)])
    return(characters)

def main (new_width=100):
    if len(sys.argv) <= 1 :
        print('You must provide one argument: [path to source image]')
        return
    
    try:
        image = PIL.Image.open(sys.argv[1])
    except:
        print(sys.argv[1], 'Is not a valid pathname to an image')
    
    new_image_data = pixels_to_ascii(grayfy(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)

main()
