#!/usr/bin/python -O

import sys

addressCount = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    thisKey, thisCount = data_mapped
    
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", addressCount)
        oldKey = thisKey;
        addressCount = 0

    oldKey = thisKey
    addressCount += float(thisCount)

if oldKey != None:
    print(oldKey, "\t", addressCount)