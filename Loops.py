import math

n = int(input())

if(n>=1 and n<=20):
    for i in range(n):
        print(int(math.pow(i, 2)))