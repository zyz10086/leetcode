# 如果不缺内存，如何使用一个具有库的语言来实现一中排序算法以表示和排序集合

import random
import time,datetime 
import numpy as np
import matplotlib.pyplot as plt
from  bitarray import bitarray


def mock_data():
    datas = []
    for i in range(100000000):
        datas.append(i)
    random.shuffle(datas)
    return datas



def quick_sort(datas,left_i,right_i):
    #选出一个变量当作比较值
    head = datas[left_i]
    left_point,right_point = left_i+1,right_i
    while(left_point<right_point):
        while(datas[left_point]<=head and left_point < right_i):
            left_point+=1
        while(datas[right_point]>=head and right_point > left_i ):
            right_point-=1
        if(left_point < right_point):
            tmp = datas[left_point]
            datas[left_point] = datas[right_point]
            datas[right_point] = tmp
    if(head > datas[right_point]):
        datas[left_i] = datas[right_point]
        datas[right_point] = head
    if(left_i<right_point-1):
        quick_sort(datas,left_i,right_point-1)
    if(right_point+1<right_i):
        quick_sort(datas,right_point+1,right_i)

def bit_map_sort(datas):
    bit_datas = bitarray(len(datas))
    for i in  datas:
        bit_datas[i] = 1
    res = []
    for i in range(len(bit_datas)):
        if(bit_datas[i]==1):
            res.append(i)
    return res
    
datas = mock_data()
print(datetime.datetime.now())
# quick_sort(datas,0,len(datas)-1)
# print(datetime.datetime.now())
# print(datas[0:100],datas[len(datas)-100:len(datas)])
bit_map_sort(datas)
print(datetime.datetime.now())
list.sort(datas)
print(datetime.datetime.now())
print(datas[0:100],datas[len(datas)-100:len(datas)])