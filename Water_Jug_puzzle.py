
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:43:50 2020

@author: deepc
"""
class graph :
    j1=int(input("Enter j1 :"))
    j2=int(input("Enter j2 :" ))
    limit=int(input("Enter final cap :"))
    node = int()
    parent = int()
    a = int ()
    b = int ()
    n =-1
    c = 1
    visited = {1 : [0,0]}
    
def fillJ1(obb = graph(),p = int()) :
    graph.n = graph.n+1
    dict[graph.n] = graph()
    dict[graph.n].node = graph.n
    dict[graph.n].a=graph.j1
    dict[graph.n].b=obb.b
    dict[graph.n].parent = p
    pp = dict[graph.n].node
    temp = []
    temp = [dict[graph.n].a , dict[graph.n].b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    if check == 0:
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(dict[graph.n].a)
        graph.visited[graph.c].append(dict[graph.n].b)
        fillJ2(dict[graph.n],pp)
        J1toJ2(dict[graph.n],pp)
        emptyj2(dict[graph.n],pp)
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b
        
    
def fillJ2(obb = graph(),p = int()) :
    graph.n = graph.n+1
    dict[graph.n] = graph()
    dict[graph.n].node = graph.n
    dict[graph.n].a=obb.a
    dict[graph.n].b=graph.j2
    dict[graph.n].parent = p
    pp = dict[graph.n].node
    temp = []
    temp = [dict[graph.n].a , dict[graph.n].b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    if check == 0:
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(dict[graph.n].a)
        graph.visited[graph.c].append(dict[graph.n].b)
        fillJ1(dict[graph.n],pp)
        J2toJ1(dict[graph.n],pp)
        emptyj1(dict[graph.n],pp)
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b

def emptyj1(obb = graph(),p = int()) :
    graph.n = graph.n+1
    dict[graph.n] = graph()
    dict[graph.n].node = graph.n
    dict[graph.n].a=0
    dict[graph.n].b=obb.b
    dict[graph.n].parent = p
    pp = dict[graph.n].node
    temp = []
    temp = [dict[graph.n].a , dict[graph.n].b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    
    if check == 0:
        graph.c = graph.c +1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(dict[graph.n].a)
        graph.visited[graph.c].append(dict[graph.n].b)
        fillJ2(dict[graph.n],pp)
        J2toJ1(dict[graph.n],pp)
        emptyj2(dict[graph.n],pp)
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b

def emptyj2(obb = graph(),p = int()) :
    graph.n = graph.n+1
    dict[graph.n] = graph()
    dict[graph.n].node = graph.n
    dict[graph.n].a=obb.a
    dict[graph.n].b=0
    dict[graph.n].parent = p
    pp = dict[graph.n].node
    temp = []
    temp = [dict[graph.n].a , dict[graph.n].b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    
    if check == 0:
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(dict[graph.n].a)
        graph.visited[graph.c].append(dict[graph.n].b)
        fillJ1(dict[graph.n],pp)
        J1toJ2(dict[graph.n],pp)
        emptyj1(dict[graph.n],pp)
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b


def J1toJ2(obb = graph(),p = int()) :
    graph.n = graph.n+1
    dict[graph.n] = graph()
    dict[graph.n].node = graph.n
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b
    empty=graph.j2-obb.b
    if dict[graph.n].a<=empty:
        dict[graph.n].b=dict[graph.n].b+dict[graph.n].a
        dict[graph.n].a=0
    else:
        dict[graph.n].a=dict[graph.n].a-empty
        dict[graph.n].b=graph.j2
    
    dict[graph.n].parent = p
    pp= dict[graph.n].node
    temp = []
    temp = [dict[graph.n].a , dict[graph.n].b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    
    if check == 0:
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(dict[graph.n].a)
        graph.visited[graph.c].append(dict[graph.n].b)
        fillJ1(dict[graph.n],pp)
        J2toJ1(dict[graph.n],pp)
        emptyj2(dict[graph.n],pp)
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b


def J2toJ1(obb = graph(),p = int()) :
    graph.n = graph.n+1
    dict[graph.n] = graph()
    dict[graph.n].parent = p
    dict[graph.n].node = graph.n
    pp = dict[graph.n].node
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b
    empty=graph.j1-obb.a
    if dict[graph.n].b<=empty:
        dict[graph.n].a=dict[graph.n].a+dict[graph.n].b
        dict[graph.n].b=0
    else:
        dict[graph.n].b=dict[graph.n].b-empty
        dict[graph.n].a=graph.j1
    temp = []
    temp = [dict[graph.n].a , dict[graph.n].b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    if check == 0:
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(dict[graph.n].a)
        graph.visited[graph.c].append(dict[graph.n].b)
        emptyj1(dict[graph.n],pp)
        fillJ2(dict[graph.n],pp)
        J1toJ2(dict[graph.n],pp)
    dict[graph.n].a=obb.a
    dict[graph.n].b=obb.b

dict = {}
graph.n = graph.n+1
dict[graph.n] = graph()
dict[graph.n].node=graph.n
dict[graph.n].parent=-1
dict[graph.n].a=0
dict[graph.n].b=0
fillJ1(dict[graph.n])
fillJ2(dict[graph.n])
print(graph.visited)
final =int()
for i in range(graph.n):
    if dict[i].a==0 and dict[i].b==graph.limit:
        final = i
        break
graph.n=final
while dict[graph.n].parent > -1 :
    print(dict[graph.n].a,dict[graph.n].b)
    graph.n=dict[graph.n].parent
print(dict[graph.n].a,dict[graph.n].b)


