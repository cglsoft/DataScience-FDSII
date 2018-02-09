#!/usr/bin/python

import sys

numberOfOcorr = 0
totalPath     = 0
mostPopular   = None
oldKey        = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisPath = data_mapped

    if oldKey and oldKey != thisKey:
        if totalPath > numberOfOcorr:
            numberOfOcorr = totalPath        
            mostPopular = oldKey
            print( " Popular : {0} - Occurrences : {1}".format(oldKey,totalPath))
        totalPath = 0

    oldKey    = thisKey
    totalPath += 1


print("The most popular file is ",mostPopular,"\t","The number of occurrences is ",float(numberOfOcorr))