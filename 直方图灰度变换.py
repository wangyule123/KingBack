# coding=utf-8

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("E:/big data/emo1.jpg", cv2.IMREAD_COLOR)
#最大值法
MaxGary = np.zeros(img.shape[:2], dtype="uint8")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        MaxGary[i, j] = max(img[i, j][0], img[i, j][1], img[i, j][2])
    cv2.namedWindow('MaxGary', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('MaxGary', 320, 175)
    cv2.imshow('MaxGary', MaxGary)
    cv2.moveWindow('MaxGary', 0, 0)

#均值法
NolGary = np.zeros(img.shape[:2], dtype="uint8")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        NolGary[i, j] = int((img[i, j][0] + img[i, j][1] + img[i, j][2]) / 3)
    cv2.namedWindow('NolGary', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('NolGary', 320, 175)
    cv2.imshow('NolGary', NolGary)
    cv2.moveWindow('NolGary', 330, 0)

#加权均值法
PeoGary = np.zeros(img.shape[:2], dtype="uint8")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        PeoGary[i, j] = 0.114 * img[i, j][0] + 0.578 * img[i, j][1] + 0.299 * img[i, j][2]
    cv2.namedWindow('PeoGary', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('PeoGary', 320, 175)
    cv2.imshow('PeoGary', PeoGary)
    cv2.moveWindow('PeoGary', 660, 0)


cv2.waitKey()
