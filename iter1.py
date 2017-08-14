from itertools import *
#import numpy

K, M = map(int, input().split())
N = []

for i in range(K):
     N.append(map(int, input().split()))        
MAX = -1
l=list(product(*N))
#for i in :
 #   MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
print(l)