# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 300
IMAGE_LOAD_TIME = 1000
# These are the constants for the image size. 
image = Image(IMAGE_URL)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
# This adds the image to the canvas. 
add(image)

"""
 Filter that takes an image as a parameter
 and applies a filter, then returns the filtered image
"""
# This will make a list of color values. 
def list_pixel(pixel):
    new_color = (pixel[0] + pixel[1] + pixel[2]) // 3
    return new_color
    
# This function will change each pixel in the image. They will become muted
# and have a green hint to it. 
def custom_filter(iamge):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_color = list_pixel(pixel)
            image.set_red(x, y, 00)
            image.set_green(x, y, new_color)
            image.set_blue(x, y, 100)
# This will call the function to change the image. 
def change_image():
    global image
    image = custom_filter(image)
# This will print will take a minute while the image is being changed.     
print("Might take a minute....")   
timer.set_timeout(change_image, IMAGE_LOAD_TIME)