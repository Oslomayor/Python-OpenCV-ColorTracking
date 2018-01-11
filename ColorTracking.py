# coding: UTF-8
# 2018.1.3
# @dormitory
# 数字图像处理大作业
# 原图待识别红色区域的像素
# R：220-120
# G：100-50
# B：100-50

# 导入 OpenCV2
import cv2
import numpy as np
# 目标区域的RGB颜色空间的值
Rmax = 255
Rmin = 120
Gmax = 100
Gmin = 50
Bmax = 100
Bmin = 50
# 目标区域的坐标
top = 0
bottom = 0
left = 0
right = 0

# HSV参数待调
# lower_red = np.array([80, 50, 170])
# upper_red = np.array([130, 148, 220])

# 图片路径
content = "D:\Python\Python36\pictures\\"
# 读取图片
img = cv2.imread(content+"lz.jpg")
# 获取图片尺寸
high = img.shape[0]
width = img.shape[1]
print("High = {0}, width = {1}".format(high, width))
# 显示原图
cv2.imshow("src", img)
# 遍历图片的像素点
# 把目标颜色以外的像素置黑
# OpenCV 中图片像素的颜色数据顺序是 B G R
im = img.copy()
for i in range(0, high, 1):
    for j in range(0, width):
        if im[i, j, 0] >= Bmin and im[i, j, 0] <= Bmax and im[i, j, 1] >= Gmin and \
                im[i, j, 1] <= Gmax and im[i, j, 2] >= Rmin and im[i, j, 2] <= Rmax:
            pass
        else:
            im[i, j] = [0, 0, 0]
cv2.imshow("separate red", im)
# 形态学滤波
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilated = cv2.dilate(im, kernel, iterations = 15)
eroded = cv2.erode(dilated, kernel, iterations = 25)
im = cv2.dilate(eroded, kernel, iterations = 13)
cv2.imshow("filtered", im)

flag = 0
# 找顶
for i in range(int(high/3), high):
    for j in range(0, width):
        if im[i, j, 0] != 0:
            flag = 1
            top = i
            break
    if flag == 1:
        break
flag = 0
# 找底
for i in range(int(2*high/3), 0, -1):
    for j in range(0, width):
        if im[i, j, 0] != 0:
            flag = 1
            bottom = i
            break
    if flag == 1:
        break
flag = 0
# 找左边
for j in range(int(width/3), width):
    for i in range(int(high/3), high):
        if im[i, j, 0] != 0:
            flag = 1
            left = j
            break
    if flag == 1:
        break
flag = 0
# 找右边
for j in range(int(2*width/3), 0, -1):
    for i in range(int(high/4), high):
        if im[i, j, 0] != 0:
            flag = 1
            right = j
            break
    if flag == 1:
        break
print("top = {top}, bottom = {bottom}".format(top=top, bottom=bottom))
print("left = {left}, right = {right}".format(left=left, right=right))
# 画定位框t
# ----------------->X
# |
# |
# |     Screen
# |
# |
# Y
# 调用 rectangle() 函数画定位框
# cv2.rectangle(scr, (左上(x,y), 右下(x,y), (B, G, R), size)
cv2.rectangle(img, (left, top), (right, bottom), (255, 50, 50), 2)
cv2.imshow("res", img)
cv2.waitKey(0)
