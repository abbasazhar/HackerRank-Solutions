#!/bin/python3

import math
import os
import random
import re
import sys



def birthdayCakeCandles(candles):
    a=max(candles)
    b=0
    for i in candles:
        if i==a:
            b=b+1
    return(b)
            
        
        
        
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
