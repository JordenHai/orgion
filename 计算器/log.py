#-*- coding:utf-8 -*-
import numpy as np

l = [0.5,0.2,0.16,0.1,0.04]
L = [0,0.5,0.7,0.86,0.96,1]
M = [0,0.3,0.5,0.7,0.85,1]
for i in range(5):
    s = []
    num = 1/l[i]
    num = np.log2(num)
    num = float(num)
    s.append(num)
    print(s)

def dec2bin(x):
  x -= int(x)
  bins = []
  while x:
    x *= 2
    bins.append(1 if x>=1. else 0)
    x -= int(x)
  return bins
sum = []
for i in range(6):
    num = dec2bin(L[i])
    sum.append(num)

print(sum[0])
print(sum[1])
print(sum[2])
print(sum[3])
print(sum[4])

