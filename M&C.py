# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:53:57 2020

@author: deepc
"""

class State:
    
    def __init__(self, m, c, b, parent):
        self.m = m
        self.c = c
        self.b = b
        self.parent = parent
        self.children = []
    
    def print_it(self):
        print('msionaries:', self.m, 'cnibals:', self.c)
    
    def Goal(self):
        if self.m == 0 and self.c == 0 and self.b == False:
            return True
        return False
    
    def createChildren(self):
        if self.b:
            c = 4
            for m in range(5):
                if (self.m - int(m/2)) >= 0 and (self.c - int(c/2)) >= 0:
                    if ((self.m - int(m/2)) == (self.c - int(c/2))) or (self.m - int(m/2)) == 0 or (self.m - int(m/2)) == 3:
                        self.children.append(State((self.m - int(m/2)), (self.c - int(c/2)), False, self))
                c -= 1
        else:
            c = 4
            for m in range(5):
                if (self.m + int(m/2)) <= 3 and (self.c + int(c/2)) <= 3:
                    if ((self.m + int(m/2)) == (self.c + int(c/2))) or (self.m + int(m/2)) == 3 or (self.m + int(m/2)) == 0:
                        self.children.append(State((self.m + int(m/2)), (self.c + int(c/2)), True, self))
                c -= 1

def BFS(head):
    queue = []
    visited = []    
    queue.append(head)
    visited.append([head.m, head.c, head.b])
    while queue:
        cur = queue.pop(0)
        
        if cur.Goal():
            return cur
        cur.createChildren()
        for child in cur.children:
            tmp = [child.m, child.c, child.b]
            if tmp not in visited:
                queue.append(child)
                visited.append(tmp)

def getParents(solution):
    path = []
    path.append(solution)
    state = solution.parent
    while state:
        path.insert(0, state)
        state = state.parent
    return path

def __main__():
    head = State(3, 3, True, None)
    solution = BFS(head)
    path = getParents(solution)

    if path is not None:
        for state in path:
            state.print_it()
    else:
        print('No solution found')
        
if __name__ == "__main__":
    __main__()