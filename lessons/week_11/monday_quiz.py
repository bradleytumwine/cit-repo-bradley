import numpy as np
import statistics as st
from random import randint

#Question One
#What is the output of the following code?
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=a+b
# print(c)

#Question Two
arr=np.array([0,0,0,0,0,0,0,0,0,0])
arr2=arr.reshape(2,5)
print(arr2)

#Question Three
data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
datas=np.array(data)
mean=np.mean(datas)
median=np.median(datas)
mode=st.mode(datas)
standard_dev=st.stdev(datas)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {standard_dev}")

#Question Four
arr=np.array([randint(1,9) for i in range(64)])
shaped_array=arr.reshape(2,2,2,2,2,2)
#confirmation
print(shaped_array.ndim)
print(shaped_array)

#Question Five
arr=np.array([
    [
        [1,2,3],[3,2,1]
    ],
    [
        [4,5,6],[6,5,4]
    ],
    [
        [7,8,9],[9,8,7]
    ]
])
arr2=arr.reshape(2,9)
print(arr2)

#Question Six
data=[[1,2,3],[4,5,6],[7,8,9]]
datas=np.array(data)
One_D_array=datas.flatten()
print(One_D_array)
