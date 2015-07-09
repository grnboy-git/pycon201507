# Procon201507
# coding: utf-8

# import
import sys
import datetime
import itertools
import re

# input
input_lines = sys.stdin.readlines()

# validation
regexp = re.compile(r'^[0-9]+$')
for input_line in input_lines:
    if regexp.search(input_line) == None:
        print 'invalid input. Only half-width number'
        sys.exit()

# get starttime
startTime = datetime.datetime.now()

# stick length
stickLength = int(input_lines[0])

# stick number
stickNum = int(input_lines[1])

# material length list
materialLengthList = []
for input_line in input_lines[2:]:
    if len(input_line) >= 1:
        materialLengthList.append(int(input_line))

# material combination
combinationList = list(itertools.combinations(materialLengthList, 3))
combinationNum = len(combinationList)

# validation
if stickNum != int(len(materialLengthList)):
    print 'invalid stick numbre.%i %i' % (int(stickNum), int(len(materialLengthList)))
    sys.exit()

# matching combination
matchList = []
for combination in combinationList:
    if sum(combination) == stickLength:
        matchList.append(combination)

# get endtime
endTime = datetime.datetime.now()

# show result
print 'matching combination number is %i' % len(matchList)
print 'matching combination is '
print matchList
delta = endTime - startTime
print 'time is %i.%i' % (delta.seconds, delta.microseconds)
