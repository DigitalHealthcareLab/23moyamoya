import cv2
import numpy as np
import sys

image_path = sys.argv[1]

def remove_black_area(image : np.array, tol = 8) :
    """
    Change tolerance value(tol)
    """
    mask = image > tol # True if pixel value is greater than tol
    image = image[np.ix_(mask.any(1), mask.any(0))] # Remove all rows and columns that contain only black pixels (False Values)
    return image
        
def histogram_equalization(image):
    image = cv2.equalizeHist(image)
    return image

def bound_box(image):
    height, width = image.shape 
    max_size = max(height, width)
    image = cv2.copyMakeBorder(image, (max_size-height)//2, (max_size-height)//2, 0, 0, cv2.BORDER_CONSTANT, value=0) # top, bottom, left, right
    return image


def crop_circle(image : np.array):
    height, width = image.shape
    x = int(width / 2) 
    y = int(height / 2) 
    r = np.amin((x,y)) 
    circle_image = np.zeros((height, width), np.uint8)
    cv2.circle(circle_image, (x,y), int(r), 1, thickness=-1)
    image = cv2.bitwise_and(image, image, mask=circle_image)
    return image

def crop(image : np.array) : 
    height, width = image.shape
    y = int(height / 2)
    y_crop = round(y * 0.055)
    image = image[y_crop : height - y_crop]
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.stack([image, image, image], axis=-1)
    return image

if __name__ == '__main__' : 
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('step1.png', image)
    image = remove_black_area(image)
    cv2.imwrite('step2.png', image)
    image = histogram_equalization(image)
    cv2.imwrite('step3.png', image)
    image = bound_box(image)
    cv2.imwrite('step4.png', image)
    image = crop_circle(image)
    cv2.imwrite('step5.png', image)
    image = crop(image)
    cv2.imwrite('step6.png', image)
