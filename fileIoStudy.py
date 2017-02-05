# file i/o study

import sys

filePath = "./study/fileiostudy.txt"

# open("파일이름", "모드")
f = open(filePath, 'w')

f.write("Hello world\n")
for i in range(10):
	f.write("line : %d \n" % i)

f.close()

# - - - -

f = open(filePath, 'a')
for i in range(500, 510):
	f.write("line : %d \n" % i)
f.close()

# - - - -

with open(filePath, 'a') as f:
	f.write("Monty python's Flying Circus")

# - - - -

f = open(filePath, 'r')

reads = f.read()
print(reads)

f.close()


"""
readLines = f.readlines()
for line in readLines:
	print(line)

f.close()
"""


"""
f = open(filePath, 'r')

while True:
	readLine = f.readline()
	if not readLine: break;
	print(readLine)

f.close()
"""