import cv2
import numpy as np

# 读取一幅图像 第一个参数是图像路径
# 第二个参数代表读取方式，1表示3通道彩色，0表示单通道灰度
im = cv2.imread(r"E:/big data/emo1.jpg", 1)  # 路径
# 在“test”窗口显示图像im
#cv2.imshow("test1", im)
# 等待用户按键反馈
#cv2.waitKey()

# 打印图像数据的数据结构类型
# print(type(im))
# 打印图像的尺寸
# print(im.shape)

# 将图像保存到指定路径
# cv2.imwrite('C:/Users/86176/Desktop/big data/emo2.jpg', im)
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.resizeWindow('test', 640, 350)
cv2.imshow("test", im)
cv2.moveWindow('test', 650, 380)
# 使用opencv里的cvtColor进行颜色空间变化 cv2.COLOR_BGR2GRAY 代表 BGR to gray
img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Gray1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Gray1', 640, 350)
cv2.imshow("Gray1", img_gray)
cv2.moveWindow('Gray1', 0, 0)
# cv2.waitKey()

# 使用opencv里的cvtColor进行颜色空间变化 cv2.COLOR_BGR2RGB 代表 BGR to RGB
im_rgb1 = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
# 当图像数据为3通道时，imshow函数认为数据是BGR的
# 使用imshow显示RGB数据，会发现图片显示颜色畸变
cv2.namedWindow('RGB1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RGB1', 640, 350)
cv2.imshow("RGB1", im_rgb1)
cv2.moveWindow('RGB1', 650, 0)
# cv2.waitKey()

# 使用opencv里的cvtColor进行颜色空间变化 cv2.COLOR_BGR2HSV 代表 BGR to HSV
im_rgb2 = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
# 当图像数据为3通道时，imshow函数认为数据是BGR的
# 使用imshow显示HSV数据，会将HSV分量强行当做BGR进行显示
cv2.namedWindow('RGB2', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RGB2', 640, 350)
cv2.imshow("RGB2", im_rgb2)
cv2.waitKey()
cv2.moveWindow('RGB2', 0, 370)
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple widgt
# pywin32

# encoding:utf-8
import cv2
import numpy as np

# 读取图片
src = cv2.imread('C:/Users/86176/Desktop/big data/emo1.jpg')

# 图像缩放
result = cv2.resize(src, (500, 300))
print(result.shape)

# 显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
