# coding = utf-8
import os
import sys
import random

# get arg
stickLength = sys.argv[1]
stickNum = sys.argv[2]

numList = []

numList.append(stickLength)
numList.append(stickNum)

while len(numList[1:]) <= int(stickNum):
    num = random.randint(500, 2000)
    if not num in numList:
        numList.append(num)

path = os.path.abspath(os.path.dirname(__file__))
path = path + '/input2.txt'

if os.path.isfile(path):
    print 'already'
    sys.exit()
else:
    fp = open(path, "w")
    for line in numList:
        line = str(line) + '\n'
        fp.write(line)
    fp.close()
