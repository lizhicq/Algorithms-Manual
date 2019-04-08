#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. LONG_INTEGER k
#

def numberOfPairs(a, k):
    lo, hi = 0, len(a) - 1
    ans = 0
    a.sort()
    while lo < hi:
        target = a[lo] + a[hi]
        if target > k:
            hi -= 1
        elif target < k:
            lo += 1
        else:# target == k
            ans += 1
            lo += 1
            while lo < len(a) and a[lo] + a[hi] == k:
                lo += 1
    return ans


def powerJump(game):

    tar = game[-1]
    dis = 0
    start = -1
    power = 1
    for i, ch in enumerate(game):
        if ch == tar:
            dis = i - start
            start = i
            power = max(power, dis)
        else:
            pass
    return power


if __name__ == "__main__":
    a = [6, 6, 3, 9, 5, 1]
    k = 12
    print(numberOfPairs(a, k))

    game = '10101'
    print(powerJump(game))