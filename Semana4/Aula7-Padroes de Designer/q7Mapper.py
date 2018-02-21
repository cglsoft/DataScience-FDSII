#!/usr/bin/python


"""
-files dir1/dict.txt#dict1,dir2/dict.txt#dict2

# https://github.com/juandecarrion/udacity-hadoop-course/tree/master/src

Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        #words = re.findall(r"[\w']+", line[4])
        words = line[4].split(' ')
        words = map(lambda x: x.lower(), words)

        # if "fantastically" in words:
        #     writer.writerow(line)

        for word in words:
            print(word, '\t', line[0])

# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()            

