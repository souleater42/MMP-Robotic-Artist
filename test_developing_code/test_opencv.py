#!/usr/bin/env python

import cv2
import time
from PIL import Image

if __name__ == '__main__' :

    # Start default camera
    video = cv2.VideoCapture(0);

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourse#lves.

    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        #print"Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frame# s per second using video.get(cv2.CAP_PROP_FPS)")


    # Number of frames to capture
    num_frames = 12000;


    # print "Capturing {0} frames".format(num_frames)

    # Start time
    start = time.time()

    # Grab a few frames
    #for i in range(0, num_frames) :
    #    ret, frame = video.read()
    #    cv2.imwrite('testCap.jpg', frame)
    #    img = cv2.imread('testCap.jpg', 0)
    #    blur = cv2.GaussianBlur(img, (21, 21), 0)
    #    sobal = cv2.Sobel(blur, cv2.CV_64F, 1, 1, ksize=5)
    #    ret, threshold = cv2.threshold(sobal, 25, 255, cv2.THRESH_BINARY_INV)
    #    cv2.imshow("cap", sobal)
    #    if cv2.waitKey(1) & 0xFF == ord('q'):
    #        break

    img = cv2.imread('testCap.jpg', 0)
    #blur = cv2.GaussianBlur(img, (5, 5), 0)
    #sobal = cv2.Sobel(blur, cv2.CV_64F, 1, 1, ksize=5)
    #ret, threshold = cv2.threshold(sobal, 25, 255, cv2.THRESH_BINARY_INV)
    #for x in range(0, threshold.shape[0]):
    #    for y in range(0, threshold.shape[1]):
    #        if threshold.item(x, y) == 0:
    #            threshold.itemset((x, y), 0)
    #            print(str(x) + "," + str(y))
    canny = cv2.Canny(img, 25, 100)
    for i in range(0, num_frames):
        #threshold.itemset((100, 100), 0)
        #print(threshold.item(100, 100))
        cv2.imshow("cap", canny)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    #print "Time taken : {0} seconds".format(seconds)
    print(seconds)

    # Calculate frames per second
    fps  = num_frames / seconds;
    #print "Estimated frames per second : {0}".format(fps);
    print(fps)
    # Release video
    video.release()
