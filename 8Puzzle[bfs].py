# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:53:01 2020

@author: deepc
"""
import numpy as np

class Node:
    def __init__(self,puz):
        #puzzle is the arrangement of the digits
        #children is the frontier or the nodes to be explored
        #parent is the current node
        #pos is the position of the tile containing 0
        self.puzzle = puz[:]
        self.children = []  
        self.parent = None
        self.pos = 0
        self.level = 0
    
    #Function for taking user-input
    def TakeInput():
        print("Input numbers row-wise; i.e. 1 2 3 4 5 6 7 8 0: ")
        new_puzzle = [int(x) for x in input().split()]
        return new_puzzle
    
    #Function to check the digit zero in the puzzle    
    def CheckZero(self,puz):
        for i in range(0,9):
            if puz[i] == 0:
                return i
   
    #Function to check if goal state is reached
    def CheckGoal(self):
        GoalFlag = True
        goal = [1,2,3,4,5,6,7,8,0]
        if goal != self.puzzle:
            GoalFlag = False
            return GoalFlag
        return GoalFlag
    
    #Function to move slide up
    def SlideUp(self):
        if(self.pos!=0 and self.pos!=1 and self.pos!=2):
            puz = self.puzzle[:]
            #swap the digits
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos-3]
            puz[self.pos-3] = temp
            child = Node(puz)
            #child = Node(puz, self.level + 1)
            #append to frontier/children list
            self.children.append(child)
            #self.level = self.level + 1
            #make parent node as current node
            child.parent = self
    
    #Function to move slide right
    def SlideRight(self):
        if(self.pos%3 < 2):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos+1]
            puz[self.pos+1] = temp
            child = Node(puz)
            #child = Node(puz, self.level + 1)
            self.children.append(child)
            #self.level = self.level + 1
            child.parent = self
    
    #Function to move slide down
    def SlideDown(self):
        if(self.pos!=6 and self.pos!=7 and self.pos!=8):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos+3]
            puz[self.pos+3] = temp
            child = Node(puz)
            #child = Node(puz, self.level + 1)
            self.children.append(child)
            #self.level = self.level + 1
            child.parent = self
    
    #Function to move slide left
    def SlideLeft(self):
        if(self.pos%3 != 0):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos-1]
            puz[self.pos-1] = temp
            child = Node(puz)
            #child = Node(puz, self.level + 1)
            self.children.append(child)
            #self.level = self.level + 1
            child.parent = self
    
    #Function to slide tile in all possible directions, to generaye child nodes
    def PuzzleIteration(self):
        self.pos = self.CheckZero(self.puzzle)        
        self.SlideRight()
        self.SlideDown()
        self.SlideLeft()
        self.SlideUp()
        #print("iter")
    
    #Function to display puzzle 
    def DisplayPuzzle(self):
        print()
        c = 0
        for i in range(3):
            for j in range(3):
                print(self.puzzle[c], end = " ")
                #print(" ")
                c = c + 1
            print()    
    
#Breadth first search algorithm to solve the 8 puzzle        
def BFSalgo(root):
    #set used for quick searching of visited states
    visited_nodes = set()
    frontier = []
    visited_nodes.add(str(root.puzzle))
    frontier.append(root)
    print("Solving...")
    #return 0
    while True:        
        CurrentPuzzle = frontier.pop(0)
        #Check if goal position is reached
        if CurrentPuzzle.CheckGoal():
            solution = []
            solution.append(CurrentPuzzle)
            #Tracing the moves to get to goal position
            while CurrentPuzzle.parent != None:
                CurrentPuzzle = CurrentPuzzle.parent
                solution.append(CurrentPuzzle)               
            print("Puzzle solved")
            print("Total configurations explored: "+str(len(visited_nodes)))
            print("Moves for reaching the goal state: "+str(len(solution)-1))
            return solution, visited_nodes
        #Iterating all the possible moves for a particular node
        CurrentPuzzle.PuzzleIteration()
        for i in range(len(CurrentPuzzle.children)):
            ToBeExplored = CurrentPuzzle.children[i]
            #Checking if iteration already explored, if not so it is added to
            #explored
            if(not str(ToBeExplored.puzzle) in visited_nodes):
                frontier.append(ToBeExplored)
                visited_nodes.add(str(ToBeExplored.puzzle))                           
                                       

if __name__ == "__main__":
    count = 0
    puzzle = Node.TakeInput()
    #Create object root from class Node
    root = Node(puzzle)
    #check solvabiity
    for i in range(0,8):
        for j in range(i,9):
            if(puzzle[i] > puzzle[j] and puzzle[j] != 0):
                count = count + 1
    if count % 2 == 1:
        print("No solution exists")
    else:
        print("Solution exists")
        sol, visited = BFSalgo(root)
        sol.reverse()
        for i in range(len(sol)):
            sol[i].DisplayPuzzle()
        print()
        print("Writing to files; may take some time")
        print()
        #Writing puzzle data to files
        file = open("nodePath.txt", "w")
        for i in range(len(sol)):
            temp = np.array(sol[i].puzzle).reshape((3,3))
            temp = temp.T.reshape(1,9)
            file.write(str(temp[0][0])+' '+str(temp[0][1])+' '+str(temp[0][2])+
                       ' '+str(temp[0][3])+' '+str(temp[0][4])+' '+str(temp[0][5])+' '
                       +str(temp[0][6])+' '+str(temp[0][7])+' '+str(temp[0][8])+'\n')
        file.close()
        print("nodePath.txt updated")
        print()
        print("Now updating Nodes.txt")
        #Writing explored nodes/puzzles to file
        file = open("Nodes.txt", "w")
        for i in range(len(visited)):
            temp2 = np.array(list(visited)[i])
            file.write(str(list(visited)[i][1])+' '+str(list(visited)[i][10])+' '+
                       str(list(visited)[i][19])+' '+str(list(visited)[i][4])+' '+
                       str(list(visited)[i][13])+' '+str(list(visited)[i][22])+' '+
                       str(list(visited)[i][7])+' '+str(list(visited)[i][16])+' '+
                       str(list(visited)[i][25]) + '\n')           
        file.close()
        print()
        print("Nodes.txt updated")
        print('The File is stored in the same folder as the program')