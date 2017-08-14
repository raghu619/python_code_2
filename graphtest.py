graph={"A":set(['B','C']),
       "B":set(["A",'D','E']),
       "C":set(['A','F']),
       "D":set(['B']),
       "E":set(['B','F']),
       "F":set(['C','E'])}




def dfs(graph,start):
    visited,stack=set(),[start]
    while stack:
        vertex=stack.pop()
        if(vertex  not in visited):
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited       
print(dfs(graph,'A'))

def dfs_path(graph,start,goal):
    stack=[(start,[start])]
    while stack:
        (vertex,path)=stack.pop()
        for next in graph[vertex]-set(path):
            if(next==goal):
                yield path+[next]
            else:
                stack.append((next,path+[next]))
    
print(list(dfs_path(graph,'A','F')))    
"""from collections import Counter
from operator import itemgetter

for item in (sorted(sorted(Counter(raw_input()).items()), key = itemgetter(1), reverse = True)[:3]):
   print item[0], item[1]"""
from collections import Counter

for letter, counts in sorted(Counter(raw_input()).most_common(),key = lambda x:(-x[1],x[0]))[:3]:
    print letter, counts
