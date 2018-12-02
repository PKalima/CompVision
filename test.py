import cv2
import numpy as np
from matplotlib import pyplot as plt
import skimage.measure

def main():
    img = cv2.imread('numbers.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tempimg = img
    kernel = np.ones((1,10),np.float32)/10
    print(kernel)
    tempimg = skimage.measure.block_reduce(tempimg, (2,2), np.mean)
    print(tempimg.shape)
    '''
    roi = img[50:150, 50:150]
    img[200:300, 200:300] = roi
    '''
    plt.subplot(231),plt.imshow(img,'gray')
    plt.subplot(232),plt.imshow(tempimg,'gray')
    plt.show()
    




if __name__ == '__main__':
    main()    