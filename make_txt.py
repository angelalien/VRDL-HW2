# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:17:46 2021
@author: Lien
"""

import os
import random

# Split training, validation, and testing data
trainval_percent = 0.9
train_percent = 0.9
labelfilepath = "data/labels"
txtsavepath = "data/imageSets"
total_label = os.listdir(labelfilepath)

num = len(total_label)  # total image
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open("data/imageSets/trainval.txt", "w")
ftest = open("data/imageSets/test.txt", "w")
ftrain = open("data/imageSets/train.txt", "w")
fval = open("data/imageSets/val.txt", "w")

for i in list:
    name = total_label[i][:-4] + ".png\n"
    if i in trainval:
        ftrainval.write("data/images/" + name)
        if i in train:
            ftrain.write("data/images/" + name)
        else:
            fval.write("data/images/" + name)
    else:
        ftest.write("data/images/" + name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
