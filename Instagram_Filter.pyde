add_library('ColorScheme')
def setup():
    size(800, 550)
    loadPixels() # load pixels into the list
    print(len(pixels)) # print the length of the pixels list
    
    img = loadImage("IMG_1868.jpg")
    image(img, 0, 0, 800, 550)
    loadPixels()
    numPixels = width * height
    
    for i in range(numPixels):
        oldColor = pixels[i]
        r = red(oldColor) 
        g = green(oldColor) 
        b = blue(oldColor)
        
    # INVERT / GRAYSCALE
        pixels[i] = color(r, g + b / 3)
    # GENERAL
        # pixels[i] = color(r, g, b)
        
    # ENHANCES RED
        # pixels[i] = color(r, 0, 0)
    
    # GRAYSCALE
        # pixels[i] = color(r + g + b / 3)
        
    # ENHANCES BLUE
        # pixels[i] = color(0, 0, b)
    
    # ENHANCES GREEN
        # pixels[i] = color(0, g, 0)
    
    # HALF HORIZONTALLY
    # for i in range(0, len(pixels) / 2):
    #     oldColor = pixels[i]
    #     r = red(oldColor) 
    #     g = green(oldColor) 
    #     b = blue(oldColor)
    #     pixels[i] = color(r, 0, 0)
    # for i in range(len(pixels) / 2, len(pixels)):
    #     oldColor = pixels[i]
    #     r = red(oldColor) 
    #     g = green(oldColor) 
    #     b = blue(oldColor)
    #     pixels[i] = color(0, 0, b)
        
    # HALF VERTICALLY
    # for i in range (0, len(pixels)):
    #     oldColor = pixels[i]
    #     r = red(oldColor) 
    #     g = green(oldColor) 
    #     b = blue(oldColor)
    #     y = i / 800
    #     x = i % 550
    #     if x < 400 - 100:
    #         pixels[i] = color(r, 0, 0)
    #     elif y > 550:
    #         pixels[i] = color(0, 0, b)
        
    # CUT HORIZONTALLY
    
    # halfImage = width * height / 2

    # loadPixels()
    # for i in range(halfImage): 
    #     pixels[i+halfImage] = pixels[i]
    # updatePixels()
    
    updatePixels()
    
    
