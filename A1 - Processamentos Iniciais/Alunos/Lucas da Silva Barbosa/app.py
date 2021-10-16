import cv2
import sys
import numpy as np

# read flags
flags = sys.argv[1:]

try:
    # read image 
    img = cv2.imread(flags[0])

    # split image into channels
    b, g, r = cv2.split(img)

    # get flag
    flag = flags[1]
    
    if flag == '-r':
        cv2.imwrite('red.png', r)
    elif flag == '-g':
        cv2.imwrite('green.png', g)
    elif flag == '-b':
        cv2.imwrite('blue.png', b)
    elif flag == '-rgb':
        cv2.imwrite('red_green_blue.png', cv2.merge([r, g, b]))
    elif flag == '-inverted': 
        cv2.imwrite('inverted.png', cv2.bitwise_not(img))
    elif flag == '-gray_scale':
        cv2.imwrite('gray_scale.png', cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    elif flag == '-colorized_red':
        zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")
        cv2.imwrite('colorized_red.png', cv2.merge([zeros_ch, zeros_ch, r]))
    elif flag == '-colorized_green':
        zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")
        cv2.imwrite('colorized_green.png', cv2.merge([zeros_ch, g, zeros_ch]))
    elif flag == '-colorized_blue':
        zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")
        cv2.imwrite('colorized_blue.png', cv2.merge([b, zeros_ch, zeros_ch]))
    else:
        print('Invalid flag')
except:
    print("Error: No image found")
























# img = cv2.imread('test.jpg')
# blue, green, red = cv2.split(img) # Split the image into its channels

# cv2.imshow("red image", red) # Display the red channel in the image
# # Display the red channel in the image

# cv2.waitKey(0) 

# cv2.destroyAllWindows() # Close all windows