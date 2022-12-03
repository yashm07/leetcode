#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY items as parameter.
#

def getMinimumOperations(items):
    # Write your code here
    min_operations = 0
    
    for i in range(1, len(items)):
        if items[i]%2 == items[i-1]%2:
            val1 = items[i]%2
            val2 = items[i-1]%2
            count = 0
            while True:
                count += 1
                val1 = val1//2
                val2 = val2//2
                
                if val1%2 != items[i]%2:
                    items[i] = val1
                    break
                elif val2%2 != items[i-1]%2:
                    items[i-1] = val2
                    break
                
            min_operations += count
    
    return min_operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    items_count = int(input().strip())

    items = []

    for _ in range(items_count):
        items_item = int(input().strip())
        items.append(items_item)

    result = getMinimumOperations(items)

    fptr.write(str(result) + '\n')

    fptr.close()
