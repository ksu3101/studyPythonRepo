# file i/o study

import sys

# open("파일이름", "모드")
f = open('./study/fileiostudy.txt', 'w')

f.write("Hello world\n")
for i in range(10):
	f.write("%d " % i)

f.close()

