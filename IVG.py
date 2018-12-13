import numpy as np
import math
import cv2
import matplotlib.pyplot as plt


class IVG():

    def __init__(self, image, version = "IHVG"):
        self.image = image
        self.version = version

        # create an empty matrix to store k-filtered image
        self.degreeMap = np.zeros(self.image.shape)
        
        # checking each pixel with pixels after the one
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                # row check
                bar = -1
                for j2 in range(j+1, self.image.shape[1]):
                    if self.image[i,j] > bar:
                        if self.image[i,j2] > bar:
                            self.degreeMap[i,j] = self.degreeMap[i,j]+1
                            self.degreeMap[i,j2] = self.degreeMap[i,j2]+1
                            bar = self.image[i,j2]
                    else:
                        break
                
                # col check
                bar = -1
                for i2 in range(i+1, self.image.shape[0]):
                    if self.image[i,j] > bar:
                        if self.image[i2,j] > bar:
                            self.degreeMap[i,j] = self.degreeMap[i,j]+1
                            self.degreeMap[i2,j] = self.degreeMap[i2,j]+1
                            bar = self.image[i2,j]
                    else:
                        break

                # diagonal check
                i2 = i + 1
                j2 = j + 1
                bar = -1 
                while(i2 < self.image.shape[0] and j2 < self.image.shape[1]):
                    if self.image[i,j] > bar:
                        if self.image[i2,j2] > bar:
                            self.degreeMap[i,j] = self.degreeMap[i,j]+1
                            self.degreeMap[i2,j2] = self.degreeMap[i2,j2]+1
                            bar = self.image[i2,j2]
                    else:
                        break

                    i2 = i2 + 1
                    j2 = j2 + 1

                # anti-diagonal check
                i2 = i - 1
                j2 = j + 1
                bar = -1 
                while(i2 >= 0 and j2 < self.image.shape[1]):
                    if self.image[i,j] > bar:
                        if self.image[i2,j2] > bar:
                            self.degreeMap[i,j] = self.degreeMap[i,j]+1
                            self.degreeMap[i2,j2] = self.degreeMap[i2,j2]+1
                            bar = self.image[i2,j2]
                    else:
                        break

                    i2 = i2 - 1
                    j2 = j2 + 1
    
    def degreeDistribution(self):
        plt.hist(self.degreeMap.ravel(), range(60))
        plt.title("Histogram")
        plt.show()

    



def test():
    testImage = cv2.imread("campus3.jpg" , 0)
    cv2.imwrite("campus3.png", testImage)
    print(testImage.shape)
    testIVG = IVG(testImage)
    maxDegree = np.amax(testIVG.degreeMap)
    filteredImage = 255 - np.floor(testIVG.degreeMap / maxDegree * 255)
    cv2.imwrite("k-filtered-campus3.png", filteredImage)
    testIVG.degreeDistribution()

if __name__ == "__main__":
    test()



