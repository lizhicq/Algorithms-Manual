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


def encryptionValidity(instructionCount, validityPeriod, keys):
    keys = set(keys)
    keys = list(keys)
    keys.sort()
    n = len(keys)
    maxdiv = 0
    for i in range(n-1, -1, -1):
        key = keys[i]
        div = 0
        for j in range(i+1):
            if key % keys[j] == 0:
                #print(key, keys[j])
                div += 1
        maxdiv = max(maxdiv, div)
        print(key, maxdiv)

    res1 = instructionCount * validityPeriod
    res2 = maxdiv * 10**5

    if res1 >= res2:
        return (1, res2)
    return (0, res2)

if __name__ == "__main__":
    print(encryptionValidity(92153207,72708429,
                             [84,43326,31019,30340,92455,18514,98916,34254,79764,63486,54966,
                              43181,27264,37582,19198,36054,20021,72826,81201,16630,34170,62711,
                              33413,99643,93704,44210,73328,31262,86542,44454,8916,72691,
                              10359,25550,48619,27806,39625,24336,97756,87955,60978,
                              67021,85473,80076,26359,4748,90622,91913,75102,
                              39006,8861,86504,98987,52279,80740,91899,94151,
                              38827,70392,47785,8120,61494,1108,32928,76713,
                              92310,62229,57613,46366,74709,21004,36723,5073,
                              59301,31938,2375,81644,2327,92997,51050,
                              15862,97510,93486,7902,16634]))