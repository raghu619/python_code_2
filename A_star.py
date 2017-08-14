# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:56:15 2017

@author: DSLAB
"""
from collections import *
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']), 
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
         }

heuristic={'A':31,'B':45,'C':57,'D':69,'E':23,'F':0}         
actual={('A','B'):6,('A','C'):5,('B','E'):6,('B','D'):9,('E','F'):17,('C','F'):2,('F','E'):7}




def dfs_paths(graph,start,goal,heuristic,actual):
    stack=[(start, [start])]
    while stack:
        (vertex,path) = stack.pop(0)
        count=0
        k=[]
        m=defaultdict(list)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                k.append([vertex,next])
                count+=1
                if(count==2):
                     while k: 
                        subnode=k.pop(0)
                        value=tuple(subnode)
                        m[subnode[1]].append(actual[value]+heuristic[subnode[1]])
                        com=min(m.values()) 
                        x=[i for i,j in m.items() if(j==com)]
                        j=x.pop()
                        stack.append((j, path + [j]))
                elif(count==1):
                    subnode1=k.pop()
                    temp1=subnode1[1]
                    stack.append((temp1,path+[temp1]))

ans=list(dfs_paths(graph, 'A', 'F',heuristic,actual))

def find_value(ans):
    temp1=list(ans)
    k=[]
    while temp1:
      temp=temp1.pop(0)
      o=[]
      count=0    
      for i,j in enumerate(temp):
        if(i+1<len(temp)):
          o.append((j,temp[i+1]))
          count+=1
          if(count==1): 
            k.append(o)          
    return k

def calculate_value(g):
    k=[]
    for i in g:
     x=[ (actual[j])  for j in i ]
     k.append(x)
    return k

def vfx(op):
   A=[]
   temp1=op[0]
   A.append(sum(temp1))
   for i in range(len(op)): 
    if(i+1!=len(op)): 
     if(temp1!=op[i+1]):
        temp1=op[i+1]
        A.append(sum(temp1))
   return A

def results(rub,ans):
  dic=defaultdict(list)
  for i,j in enumerate(ans):  
    dic[rub[i]].append(j)
  return dic
g=find_value(ans)
print(ans)
op=calculate_value(g)
rub=vfx(op)
print(rub)
rel=results(rub,ans)  
print(*rel.get(min(rel.keys())))    
#def display(rel):
   
   
