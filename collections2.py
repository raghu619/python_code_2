from collections import *
"""from itertools import *
value=input()
for i,j in groupby(value):
    print(i,len(list(j)))
s=input()
letters=[0]*26
for letter in s:
    letters[ord(letter)-ord('a')]+=1
    print(ord(letter))
for i in range(3):
    max_letter=max(letters)
    for index in range(26):
        if max_letter==letters[index]:
            print(chr(ord('a')+index),max_letter)
            letters[index]=-1
            break

print(letters)"""
"""stack=[1,2,3,4]
stack.pop()
stack.extend("6")
print(stack)
"""
graph={"A":set(['B','C']),
       "B":set(["A",'D','E']),
       "C":set(['A','F']),
       "D":set(['B']),
       "E":set(['B','F']),
       "F":set(['C','E'])}
#print(graph["A"]-set("B"))
"""def dfs(graph,start):
    visited,stack=set(),[start]
    while stack:
        vertex=stack.pop()
        if vertex  not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

print(dfs(graph,'A'))
"""
#for next in graph["B"]-set(['A']):
 #      print(next)
 
       
def dfs_paths(graph,start,goal):
    stack=[(start,[start])]
    
    while stack:
      (vertex,path)=stack.pop()  
      for next in graph[vertex]-set(path):
         if next==goal:
             yield path+[next]
         else:
              stack.append((next,path+[next]))
              
        
    
print(list(dfs_paths(graph,"A","F")))

            





















    
