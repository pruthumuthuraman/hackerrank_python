#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total = sum(arr)
    for i in range(len(arr)):
        arr[i] = total - arr[i]
    minimum = maximum = arr[0]
    for x in arr[1:]:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    print(minimum,maximum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
