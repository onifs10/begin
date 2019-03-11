import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0 
    n = 0
    z = 0
    x = int(len(arr))
    for i in arr:
        if i < 0:
            n += 1
        elif i == 0:
            z += 1
        else:
            p += 1
    # a = int(p)
    print(round(float(p/x),x)) 
    print(round(float(n/x),x))
    print(round(float(z/x),x))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
