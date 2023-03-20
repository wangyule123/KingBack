# KingBack-picture

 图像识别可视化通用平台 General platform for image recognition visualization
 
主要代码识别过程如下：

预处理：1.图片变换、2.图像增强、3.灰度化变换、4.降噪

效果图如下：


1.![image](https://user-images.githubusercontent.com/115970071/226175767-37823457-125c-4258-bd4b-6e9a2bf0c1dd.png)



分别为test（原图）、Gray1、RGB1、RGB2（HSV）


2.图像增强，采用了七种增强算法，后续会修改，选主流




![image](https://user-images.githubusercontent.com/115970071/226175992-a5db41ae-0f90-4bcc-826a-cb255eaed8b2.png)




分别为：   # 直方图均衡增强        # 拉普拉斯算法增强     # LoG对象算法增强     # 伽马变换

 
    # CLAHE         # retinex_ssr         # retinex_msr         # test（原图）
    
    
    
3.灰度化变换，采用了主流的三种算法




![image](https://user-images.githubusercontent.com/115970071/226176215-286a80fa-dbd5-4e12-9a98-7ebfd9c1cda2.png)





分别为：#最大值法               #均值法                   #加权均值法


4.![image](https://user-images.githubusercontent.com/115970071/226318387-b4d9f6bf-e2c2-4346-a2f1-fed51afa6e35.png)


在降噪中我们选择采用中值滤波和高斯滤波算法，具体特点如上，效果图如下：




![image](https://user-images.githubusercontent.com/115970071/226320666-600e87cd-82eb-4304-b920-70f23baf286c.png)




卷积神经网络中涉及的训练参数与超参数

1. 输入图像大小:在数据集处理中将图像尺寸调整到固定大小，使不同输入图像获得相同规格的输出。

2. 卷积层超参数:卷积核尺寸、卷积核数量、卷积的步长

filter：滤波器，也就是卷积核。

kernel_size：卷积核大小。卷积核一般为奇数。卷积核的大小. 取决于要提取的特征分布和区分度.如果本身要提取的特征很小那卷积核也应该很小,卷积核太大比如16x16 vs 4x4这样的差异可能导致丢失一些局部特征。
 

stride：步长。每次卷积核做卷积时移动的距离。

padding：填充。padding参数有两项：valid | same，valid表示无填充，same表示有填充。

卷积核尺寸:经典的网络如LeNet-5、VGG-19、Inception 网络使用3×3、5×5甚至1×x1结构，而在实践中最常用的尺寸为3×3、5x5。

卷积的步长:主要用于控制输出分辨率，如果填充操作使图像大小不变，步长为2的卷积输出为输入的1/4（长宽皆为1/2），对于一些需要降分辨率操作非常有效。

3. 池化层超参数

池化层一般没有参与运算的参数，它的超参数主要是池化核尺寸、池化步长及池化方式。

池化的目的是保留大的响应值并降低分辨率，与卷积层类似，池化核尺寸一般也设定为此较小的值，如2×2、3×3等，常用的是尺寸为2x2、步长为2。此外，池化方式也是可选超参数，

“用的有最大池化（Mx Poling）、平均池化（Avamge Pooling）、K-iMax Poling等。

ReKU激活函数的作用：
是为了增加神经网络模型的非线性。否则你想想，没有激活函数的每层都相当于矩阵相乘。就算你叠加了若干层之后，无非还是个矩阵相乘罢了。所以你没有非线性结构的话，根本就算不上什么神经网络。








































1.图像格式RGB/HSV/YUV
https://zhuanlan.zhihu.com/p/95952096


