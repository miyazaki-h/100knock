#coding=utf-8
import sys

data = sys.stdin
target = sys.argv[1]
flag =0

for line in data:
    if line.startswith(":"):
        if target in line:
            flag = 1
            continue
        else:
            flag = 0
    if flag:
        print line,
        
    
        
