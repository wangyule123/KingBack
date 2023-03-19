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









分别为：#最大值法               #均值法                   #加权均值法
