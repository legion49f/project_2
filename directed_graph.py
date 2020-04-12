#!/usr/bin/env python

#Question 4

class DirectedGraph:
    
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
            
    def addDirectedEdge(self, first, second):
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
        
    def removeDirectedEdge(self, first, second):
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
            if self.graph[node][i] == 1:
                neighbors.append(i)
                
        return neighbors

class TopSort:
    
    def kahns(self, graph):
        in_degree = [0]*(graph.num_nodes) 
          
        for i in range(len(graph.graph)): 
            for j in range(len(graph.graph[i])): 
                if graph.graph[i][j] == 1:
                    in_degree[j] += 1
   
        queue = [] 
        for i in range(graph.num_nodes): 
            if in_degree[i] == 0: 
                queue.append(i) 
   
        count_of_visited_nodes = 0
        top_order = [] 
  
        while queue: # Remove while loop later
            u = queue.pop(0) 
            top_order.append(u) 
  
            for i in range(len(graph.graph[u])): 
                in_degree[i] -= 1 
                if in_degree[i] == 0: 
                    queue.append(i) 
  
            count_of_visited_nodes += 1
  
        # Check if there was a cycle
        if count_of_visited_nodes != graph.num_nodes: 
            print("There exists a cycle in the graph")
        else : 
            print(top_order) 
            
        
    # Make iterative later 
    def topologicalSort(self,v,visited,stack): 
   
        visited[v] = True
   
        for i in graph.getNeighborNodes(v): 
            if visited[i] == False: 
                self.topologicalSort(i,visited,stack) 
  
        stack.insert(0,v) 
  

    def mDFS(self, graph): 
        # Mark all the vertices as not visited 
        visited = [False]*graph.num_nodes
        stack = [] 
  
        for i in range(graph.num_nodes): 
            if visited[i] == False: 
                self.topologicalSort(i,visited,stack) 
  
        print(stack)
            



from random import randint
def createRandomDAGIter(n):
    graph = DirectedGraph()
    for i in range(n):
        graph.addNode(i)
        
    for i in range(int(n * 2)):
        first_index = randint(0, n-1)
        second_index = randint(0, n-1)
        while first_index == second_index:
            first_index = randint(0, n-1)
            second_index = randint(0, n-1)
        graph.addDirectedEdge(first_index, second_index)
    
    return graph


graph = createRandomDAGIter(1000)
#print(graph.graph)
print("Topological Sort through Kahn's algorithm:")
top_sort = TopSort()
top_sort.kahns(graph)


#graph = createRandomDAGIter(1000)
#top_sort.mDFS(graph)


print("Topological Sort through mDFS algorithm:")
top_sort.mDFS(graph)




