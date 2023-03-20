# 作者：子非鱼
# 开发日期：2023/3/16
import cv2
import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)

    # cv.destroyAllWindows()


def add_peppersalt_noise(image, n=10000):
    result = image.copy()
    # 测量图片的长和宽
    w, h = image.shape[:2]
    # 生成n个椒盐噪声
    for i in range(n):
        x = np.random.randint(1, w)
        y = np.random.randint(1, h)
        if np.random.randint(0, 2) == 0:
            result[x, y] = 0
        else:
            result[x, y] = 255
    return result


# 对图像添加高斯噪声
def add_gauss_noise(image, mean=0, val=0.01):
    size = image.shape
    # 对图像归一化处理
    image = image / 255
    gauss = np.random.normal(mean, val ** 0.05, size)
    image = image + gauss
    return image


img = cv.imread('E:/big data/emo3.jpg')
if img is None:
    print('Failed to read the image')

cv2.namedWindow('add_gauss_img', cv2.WINDOW_NORMAL)
cv2.namedWindow('GaussianBlur_img', cv2.WINDOW_NORMAL)
cv2.namedWindow('add_peppersalt_img', cv2.WINDOW_NORMAL)
cv2.namedWindow('medianBlur_img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('add_gauss_img', 300, 200)
cv2.resizeWindow('GaussianBlur_img', 300, 200)
cv2.resizeWindow('add_peppersalt_img',300, 200)
cv2.resizeWindow('medianBlur_img', 300, 200)

cv2.moveWindow('add_gauss_img', 0, 0)
cv2.moveWindow('GaussianBlur_img', 310, 0)
cv2.moveWindow('add_peppersalt_img', 0, 220)
cv2.moveWindow('medianBlur_img', 310, 220)

img = cv.imread('E:/big data/emo3.jpg')
if img is None:
    print('Failed to read the image')

img1 = add_gauss_noise(img)
cv_show('add_gauss_img', img1)

img2 = cv.GaussianBlur(img1, (3, 3), 1, 2)
cv_show('GaussianBlur_img', img2)

imgA = add_peppersalt_noise(img)
cv_show('add_peppersalt_img', imgA)

# 中值滤波，可对灰色图像和彩色图像使用
imgB = cv.medianBlur(imgA, 3)
cv_show('medianBlur_img', imgB)
# ksize变大图像变模糊
# imgC = cv.medianBlur(imgA, 9)
# cv_show('after2', imgC)

cv.waitKey(0)
