# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class graphs:
    dict={}
    
    def user_menu(self):
            print("### Choosing menu ###" )
            print("1. New node")
            print("2. New edge")
            print("3. Del a node")
            print("4: Del an edge")
            print("5. Print graph")
            print("6. Apply BFS")
            print("7. Apply DFS")
            print("8. Exit program")
                
    def user_choice(self):
        choice = 10
        while(choice!=0):
            self.user_menu()
            choice=input()
            if choice == '1':
                self.add_node()
            if choice == '2':
                self.add_edge()
            if choice == '3':
                self.del_node()
            if choice == '4':
                self.del_edge()
            if choice == '5':
                self.show_graph()
            if choice == '6':
                self.bfs()
            if choice == '7':
                self.dfs()
            if choice == '8':
                sys.exit()
            else:
                pass
                
    def add_node(self):
        print("Enter node ----->") 
        node=input()
        node=int(node)
        if node not in self.dict:
            self.dict[node]=[]
            print("Success!")
        else:
            print("Enter a differnt node!")
            
    def add_edge(self):
        print("Enter node ----->")
        n=int(input())
        print("Enter edge ----->")
        e=int(input())
        if n in self.dict and e in self.dict:
            self.dict[n].append(e)
            print('new edge inserted')
        else:
            print('node not inserted')
    
    def del_node(self):
        print('Enter node ----->')
        n=int(input())
        if n in self.dict:
            for i in self.dict:
                for values in self.dict[i]:
                    if(values == n):
                        self.dict[i].remove(values)
            del self.dict[n]
            print('Deleted')
        else:
            print('invalid input')
    
    def del_edge(self):
        print("Enter node ----->")
        n=int(input())
        print("Enter edge ----->")
        e=int(input())
        if n in self.dict and e in self.dict:
            self.dict[n].remove(e)
            print('edge deleted')
        else:
            print('invalid input')
    
    def bfs(self):
        print("Enter Start Node ----->")
        startnode=int(input())
        visited = []
        q = [startnode]
        while q:
            current_node = q.pop(0)
            if current_node not in visited:
                visited.append(current_node)
                neighbours = self.dict[current_node]
                for values in neighbours:
                    q.append(values)
        print(visited)
            
    
    def show_graph(self):
        print(self.dict)

            
            
obj = graphs()
obj.user_choice()
    