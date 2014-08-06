#!/usr/bin/python
# -*- coding:utf-8 -*-
from PIL import Image 
from PIL import ImageFilter
import time
TIME = time.time()

im=Image.open('test.jpg')
im=im.filter(ImageFilter.GaussianBlur(radius=32))

print u'高斯模糊用时',time.time()-TIME

im.show()