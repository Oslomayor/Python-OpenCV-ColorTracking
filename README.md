# Python-OpenCV-ColorTracking
## 目标
在Python–OpenCV环境下，实现从图中所有带有粉红色的物体中识别出粉红色茶杯并将其用方框标记出来
## 效果
![origin](https://github.com/Oslomayor/Python-OpenCV-ColorTracking/blob/master/origin.jpg?raw=true "origin")
![result](https://github.com/Oslomayor/Python-OpenCV-ColorTracking/blob/master/result.jpg?raw=true "result")
## 原理
通过从上下左右四个方向遍历像素点的方法来寻找到物体所在的区域的边界。从原始图片中分离红色部分，为了避免由两个红色鼠标滚轮带来的干扰，采取了形态学滤波，先腐蚀掉小块的红色块，再膨胀还原目标区域的大小。找到边界后，用 OpenCV 自带函数 rectangle() 绘制定位框。
## 使用的环境
Python 3.6.3  
其余见 requirements.txt
