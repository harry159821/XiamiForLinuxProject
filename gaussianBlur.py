#!/usr/bin/python
# -*- coding:utf-8 -*-
from PIL import Image 
from PIL import ImageFilter
import time
TIME = time.time()

im=Image.open('test.jpg')
im=im.filter(ImageFilter.GaussianBlur(radius=20))
# im=im.filter(ImageFilter.GaussianBlur(radius=100))

print u'高斯模糊用时',time.time()-TIME

im.show()
im.save('test.png')


# 考虑一下先降低像素再取高斯模糊 提高效率