#!/usr/bin/env python

#Question 3
#A
class Graph:
    
    def __init__(self):
        self.nodes = []
        self.num_nodes = 0
        self.graph = []
    
    def addNode(self,nodeVal):
        if nodeVal in self.nodes:
            print("Node " + str(nodeVal) + " already exists")
            return False
        
        else:
            self.num_nodes += 1
            self.nodes.append(nodeVal)
            if self.num_nodes > 1:
                for node in self.graph:
                    node.append(0)
            newNode = []
            for _i in range(self.num_nodes):
                newNode.append(0)
            self.graph.append(newNode)
            
    def addUndirectedEdge(self, first, second):
        if first not in self.nodes:
            print("Node " + str(first) + " does not exist")
            
        if second not in self.nodes:
            print("Node " + str(second) + " does not exist")
            
        i=0
        first_index = 0
        second_index = 0
        while i < len(self.nodes):
            if self.nodes[i] == first:
                first_index = i
            if self.nodes[i] == second:
                second_index = i
                
            i = i+1
            
        self.graph[first_index][second_index] = 1
        self.graph[second_index][first_index] = 1
        
    def removeUndirectedGraph(self, first, second):
        if first not in self.nodes:
            print("Node " + str(first) + " does not exist")
            
        if second not in self.nodes:
            print("Node " + str(second) + " does not exist")
            
        i=0
        first_index = 0
        second_index = 0
        while i < len(self.nodes):
            if self.nodes[i] == first:
                first_index = i
            if self.nodes[i] == second:
                second_index = i   
            i+=1
            
        self.graph[first_index][second_index] = 0
        self.graph[second_index][first_index] = 0
        
    def getAllNodes(self):
        return self.nodes
    
    def getNeighborNodes(self, node):
        neighbors = []
        for i in range(len(self.nodes)):
            if self.graph[node][i] == 1:
                neighbors.append(i)
                
        return neighbors


import sys
class GraphSearch:
    
    def DFSRec(self, graph, start, end):
        visited = [False] * graph.num_nodes
        path = []
        path = self.DFS(graph, visited, start, end, path)
        return path
                
    def DFS(self, graph, visited, start, end, path):
        if len(path) > 0:
            if path[-1] != end:
                path.append(start)
                
        elif len(path) == 0:
            path.append(start)
        
        if start == end:
            return path
        
        visited[start] = True
        flag = 0
        if len(graph.getNeighborNodes(start)) > 0:
            for neighbor in graph.getNeighborNodes(start)[::-1]:
                if visited[neighbor] == False:
                    self.DFS(graph, visited, neighbor, end, path)
                    if path[len(path) - 1] == end:
                        return path
                    flag = 1
                    
        if flag == 0:
            del path[-1]
            
        
                
    def DFSIter(self, graph, start, end):
        visited = [False for i in range(graph.num_nodes)]  
        path = []
        stack = []  
        stack.append(start)  
  
        while (len(stack)):   # Remove while loop later..
            s = stack[-1]  
            stack.pop() 
            if (not visited[s]):  
                path.append(s)
                visited[s] = True
                
            if s == end:
                return path
  
            for node in graph.getNeighborNodes(s):  
                if (not visited[node]):  
                    stack.append(node) 
                    
                    
    def BFTRec(self, graph):
        visited = [False] * graph.num_nodes
        path = []
        queue = []
        queue.append(0)
        visited[0] = True
        self.BFS(graph, visited, queue, path)
        return path
        
    def BFS(self, graph, visited, queue, path):
        if len(queue) == 0:
            return path
        
        s = queue[0]
        queue.pop(0)
        path.append(s)
        for node in graph.getNeighborNodes(s):
            if (not visited[node]):
                visited[node] = True
                queue.append(node)
            
        self.BFS(graph, visited, queue, path)
                    
    def BFTIter(self, graph):
        visited = [False] * graph.num_nodes 
        queue = [] 
        path = []
        queue.append(0) 
        visited[0] = True
        
        while queue: # remove while loop later
            s = queue.pop(0) 
            path.append(s)
            
            for i in graph.getNeighborNodes(s): 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
                    
        return path

#Question 3
#B
from random import randint 
def createRandomUnweightedGraphIter(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
        
    for i in range(int(n*2)):
        first_index = randint(0, n-1)
        second_index = randint(0, n-1)
        while first_index == second_index:
            first_index = randint(0, n-1)
            second_index = randint(0, n-1)
        graph.addUndirectedEdge(first_index, second_index)
    
    return graph

#Question 3
#C
def createLinkedList(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
        
    for i in range(n-1):
        graph.addUndirectedEdge(i, i+1)
        
    return graph


def printPath(path):
    print()
    for node in path:
        print(node, end=" -> ")
    print()

def BFTRecLinkedList(graph):
    graph_search = GraphSearch()
    print(graph_search.BFTRec(graph))
    
def BFTIterLinkedList(graph):
    graph_search = GraphSearch()
    print(graph_search.BFTIter(graph))


graph = createRandomUnweightedGraphIter(8)
print(graph.graph)
graph_search = GraphSearch()
print("Recursive Depth-First Search", end=": ")
printPath(graph_search.DFSRec(graph, 1, 4))
print("Iterative Depth-First Search", end=": ")
printPath(graph_search.DFSRec(graph, 1, 4))
print("Iterative Breadth-First Search", end=":")
printPath(graph_search.BFTIter(graph))
print("Recursive Breadth-First Search", end=": ")
printPath(graph_search.BFTIter(graph))


graph = createLinkedList(1000) # 1000 <---recusion depth exceeded past much more than this
BFTIterLinkedList(graph)

