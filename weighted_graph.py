#!/usr/bin/env python

#Question 5

class WeightedGraph:
    
    def __init__(self):
        self.nodes = []
        self.num_nodes = 0
        self.graph = []
    
    def addNode(self,nodeVal):
        if nodeVal in self.nodes:
            print("Node " + str(nodeVal) + " already exists")
            return
        
        else:
            self.num_nodes = self.num_nodes + 1
            self.nodes.append(nodeVal)
            if self.num_nodes > 1:
                for node in self.graph:
                    node.append(0)
            newNode = []
            for _i in range(self.num_nodes):
                newNode.append(0)
            self.graph.append(newNode)
            
    def addWeightedEdge(self, first, second, weight):
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
            
        self.graph[first_index][second_index] = weight
        
    def removeWeightedEdge(self, first, second):
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
            
        self.graph[first_index][second_index] = 0
        
    def getAllNodes(self):
        return self.nodes
    
    def getNeighborNodes(self, node):
        neighbors = []
        for i in range(len(self.nodes)):
            if self.graph[node][i] > 0:
                neighbors.append(i)
                
        return neighbors

from random import randint
def createRandomCompleteWeightedGraph(n):
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(i)
        
    for i in range(int(n * (n-1))):
        first_index = randint(0, n-1)
        second_index = randint(0, n-1)
        while first_index == second_index:
            first_index = randint(0, n-1)
            second_index = randint(0, n-1)
        graph.addWeightedEdge(first_index, second_index, randint(1, 10))
    
    return graph


def createLinkedList(n):
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(i)
        
    for i in range(n-1):
        graph.addWeightedEdge(i, i+1, 1)
        
    return graph


from sys import maxsize as biggest_int # gets biggest int size aka infinity here
def minDistance(graph, dist, sptSet):  
    min = biggest_int
  
    for v in range(graph.num_nodes): 
        if dist[v] < min and sptSet[v] == False: 
            min = dist[v] 
            min_index = v 
  
    return min_index 
  

def dijkstra(graph, src):
  
    dist = {}
    i=0
    while i < graph.num_nodes:
        dist[i] = biggest_int
        i+=1
    dist[src] = 0
    sptSet = [False] * graph.num_nodes 
  
    for _node in range(graph.num_nodes): 
        u = minDistance(graph, dist, sptSet) 
  
        # Put the minimum distance vertex in the  
        # shotest path tree 
        sptSet[u] = True
  
        for v in range(graph.num_nodes): 
            if graph.graph[u][v] > 0 and sptSet[v] == False and  dist[v] > dist[u] + graph.graph[u][v]: 
                dist[v] = dist[u] + graph.graph[u][v] 
  
    return dist 


graph = createRandomCompleteWeightedGraph(10)
print(graph.graph)


print("Calculating the shortest distance from 0 node to all the other nodes:")
dist = dijkstra(graph, 0)
print(dist)
print(biggest_int)



