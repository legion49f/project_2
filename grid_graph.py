#!/usr/bin/env python

#Question 6

class GridNode:
    
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

class GridGraph:
    
    def __init__(self):
        self.nodes = []
        self.num_nodes = 0
        self.graph = []
    
    def addGridNode(self, x, y, nodeVal):
        grid_node = GridNode(x, y, nodeVal)
        
        self.num_nodes = self.num_nodes + 1
        self.nodes.append(grid_node)
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
            if self.nodes[i].x == first.x and self.nodes[i].y == first.y:
                first_index = i
            if self.nodes[i].x == second.x and self.nodes[i].y == second.y:
                second_index = i
                
            i = i+1
        if (self.nodes[first_index].x - self.nodes[second_index].x <= 1 and self.nodes[first_index].x - self.nodes[second_index].x >= 0):
            if (self.nodes[first_index].y - self.nodes[second_index].y == 0):
                    self.graph[first_index][second_index] = 1
                    self.graph[second_index][first_index] = 1
                        
                        
        if (self.nodes[first_index].y - self.nodes[second_index].y <= 1 and self.nodes[first_index].y - self.nodes[second_index].y >= 0):
                if (self.nodes[first_index].x - self.nodes[second_index].x == 0):
                    self.graph[first_index][second_index] = 1
                    self.graph[second_index][first_index] = 1
                        
                        

        
    def removeUndirectedEdge(self, first, second):
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
        self.graph[second_index][first_index] = 0
        
    def getAllNodes(self):
        return self.nodes
    
    def getNeighborNodes(self, node):
        neighbors = []
        for i in range(len(self.nodes)):
            if self.graph[node][i] == 1:
                neighbors.append(i)
                
        return neighbors
    
            
    def getIndex(self, x, y):
        for i in range(len(self.nodes)):
            if (self.nodes[i].x == x and self.nodes[i].y == y):
                return i

import random
def createRandomGraph(n):
    grid_graph = GridGraph()
    for i in range(n+1):
        for j in range(n+1):
            grid_graph.addGridNode(i, j, i * j)
    
    for i in range(grid_graph.num_nodes):
        for j in range(grid_graph.num_nodes):
            if ((i != j) and (grid_graph.getAllNodes()[i].x == grid_graph.getAllNodes()[j].x or grid_graph.getAllNodes()[i].y == grid_graph.getAllNodes()[j].y)):
                grid_graph.addUndirectedEdge(grid_graph.getAllNodes()[i], grid_graph.getAllNodes()[j])

                    
    return grid_graph
                

class AStarNode: # Thank you Itani!!!
    def __init__(self, parent=None, node=None):
        self.parent = parent
        self.node = node

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.node.x == other.node.x and self.node.y == other.node.y


def astar(graph, source, dest):
    # Create start and end node
    start_node = AStarNode(None, source)
    start_node.g = start_node.h = start_node.f = 0
    end_node = AStarNode(None, dest)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []
    
    max_iterations = grid_graph.num_nodes * 10
    outer_iterations = 0
    
    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        
        inner_iterations = 0
        
        outer_iterations += 1
        
        if (outer_iterations >= max_iterations):
            print("Max iterations reached. No path found")
            return

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append((current.node.x, current.node.y))
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for neighbor in graph.getNeighborNodes(graph.getIndex(current_node.node.x, current_node.node.y)):

            # Make sure walkable terrain
            if graph.graph[graph.getIndex(current_node.node.x, current_node.node.y)][neighbor] != 1:
                continue

            # Create new node
            new_node = AStarNode(current_node, graph.getAllNodes()[neighbor])

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            inner_iterations += 1
            
            if inner_iterations >= max_iterations:
                print("Max iterations reached. No path found")
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.node.x - end_node.node.x) ** 2) + ((child.node.y - end_node.node.y) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


random.seed(0)
grid_graph = createRandomGraph(10)
for i in range(len(grid_graph.graph)):
    for j in range(len(grid_graph.graph[i])):
        print(grid_graph.graph[i][j], end=", ")
    print()

source = grid_graph.getAllNodes()[0]
dest = grid_graph.getAllNodes()[grid_graph.getIndex(10, 10)]
path = astar(grid_graph, source, dest)
print(path)




