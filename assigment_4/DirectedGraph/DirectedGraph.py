'''
Created on Mar 18, 2019

@author: toni
'''

import copy
import random
import heapq

class DirectedGraph:
    
    def __init__(self, no_vertices = 0):
        '''
        Preconditions:
        -No_Vertices is an integer
        -No_Vertices >= 0
        
        Creates a Directed Graph with No_Vertices.
        Vertices have values between 0 and (No_Vertices - 1).
        '''
        self.__no_vertices = no_vertices
        self.__no_edges = 0
        self.__inMap = {}
        self.__outMap = {}
        self.__vertices = []
        for index in range(no_vertices):
            self.__inMap[index] = []
            self.__outMap[index] = []
            self.__vertices.append(index)
        
    
    def getNoVertices(self):
        '''
        Returns the number of vertices.
        '''
        
        return self.__no_vertices
    
    def getNoEdges(self):
        '''
        Returns the number of edges.
        '''
        
        return self.__no_edges
    
    def getVertices(self):
        '''
        Returns an iterator containing every vertex from the graph.
        '''
        
        for vertex in self.__vertices:
            yield vertex
    
    def addEdge(self, start, end, cost = 0):
        ''' O(deg(x) + deg(y))
        Preconditions:
        -start, end, cost integers
        -start != end
        -start, end is a vertex from the graph
        -there is no edge between start and end
        Throws:
        -ValueError if start or end are not vertices in the graph
        -ValueError if there is already an edge between start and end
        -ValueError is start == end
        
        Adds an edge from vertex START to END with the cost COST.(COST is implicitly 0)
        '''
        
        if self.isEdge(start, end):
            raise ValueError("The Edge does already exist!")
        #if (start == end):
            #raise ValueError("We cannot have an edge with endpoints being the same vertex!")
        if (start in self.__vertices and end in self.__vertices):
            self.__inMap[end].append([start, cost])
            self.__outMap[start].append([end, cost])
            self.__no_edges += 1
        else:
            raise ValueError("The Start Vertex or/and End Vertex does not exist!")
    
    def isEdge(self, start, end):
        '''
        Preconditions:
        -start, end integers
        -start, end is a vertex from the graph
        Throws:
        -ValueError if start or end are not vertices in the graph
        
        Returns True if there is an edge from start to end, and False otherwise.
        '''
        
        if (start in self.__vertices and end in self.__vertices):
            for edge in self.__outMap[start]:
                if (edge[0] == end):
                    return True
            return False
        else:
            raise ValueError("The Start Vertex or/and End Vertex does not exist!")
    
    def getInDegree(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if there is no vertex VERTEX in the graph
        
        Returns the in-bound degree of vertex.
        '''
        
        if vertex in self.__vertices:
            return len(self.__inMap[vertex])
        else:
            raise ValueError("The Vertex does not exist!")
    
    def getOutDegree(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if there is no vertex VERTEX in the graph
        
        Returns the out-bound degree of vertex.
        '''
        
        if vertex in self.__vertices:
            return len(self.__outMap[vertex])
        else:
            raise ValueError("The Vertex does not exist!")
    
    def getOutboundNeighbours(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if there is no vertex VERTEX in the graph
        
        Returns an iterator containing all out-bound neighbours of vertex VERTEX.
        '''
        
        if vertex in self.__vertices:
            for edge in self.__outMap[vertex]:
                yield edge[0]
        else:
            raise ValueError("The Vertex does not exist!")
    
    def getInboundNeighbours(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if there is no vertex VERTEX in the graph
        
        Returns an iterator containing all in-bound neighbours of vertex VERTEX.
        '''
        
        if vertex in self.__vertices:
            for edge in self.__inMap[vertex]:
                yield edge[0]
        else:
            raise ValueError("The Vertex does not exist!")
    
    def modifyCost(self, start, end, cost):
        '''
        Preconditions:
        -start, end integers
        -start, end is a vertex from the graph
        -start end is an edge of the graph 
        Throws:
        -ValueError if start or end are not vertices in the graph
        -ValueError if start end is not an edge of the graph
        
        Modifies the cost of the edge START END to COST.
        '''
        
        if not self.isEdge(start, end):
            raise ValueError("The Edge does not exist!")
        for edge in self.__outMap[start]:
            if edge[0] == end:
                edge[1] = cost
                break
        for edge in self.__inMap[end]:
            if edge[0] == start:
                edge[1] = cost
                break
    
    def getEdgeCost(self, start, end):
        '''
        Preconditions:
        -start, end integers
        -start, end is a vertex from the graph
        -start end is an edge of the graph 
        Throws:
        -ValueError if start or end are not vertices in the graph
        -ValueError if start end is not an edge of the graph
        
        Returns the cost of the edge START END.
        '''
        
        if not self.isEdge(start, end):
            raise ValueError("The Edge does not exist!")
        for edge in self.__outMap[start]:
            if edge[0] == end:
                return edge[1]
    
    def addVertex(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is not already a vertex in the graph
        Throws:
        -ValueError if vertex is already a vertex in the graph
        
        Adds vertex VERTEX to the graph.
        '''
        
        if vertex in self.__vertices:
            raise ValueError("The Vertex does already exist!")
        self.__no_vertices += 1
        self.__vertices.append(vertex)
        self.__inMap[vertex] = []
        self.__outMap[vertex] = []
    
    def removeVertex(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if vertex is not a vertex in the graph
        
        Removes vertex VERTEX from the graph.
        '''
        
        if not vertex in self.__vertices:
            raise ValueError("The Vertex does not exist!")
        
        #self.__inMap is modified by the method removeEdge, so we have to save it prior to
        #iterating through the map
        inMap = copy.deepcopy(self.__inMap[vertex]) 
        for edge in inMap:
            in_neighbour = edge[0]
            self.removeEdge(in_neighbour, vertex)
        
        outMap = copy.deepcopy(self.__outMap[vertex])
        for edge in outMap:
            out_neighbour = edge[0]
            self.removeEdge(vertex, out_neighbour)
            
        self.__inMap.pop(vertex)
        self.__outMap.pop(vertex)
        self.__no_vertices -= 1
        self.__vertices.remove(vertex)
    
    def removeEdge(self, start, end):
        '''
        Preconditions:
        -start, end integers
        -start, end is a vertex from the graph
        -start end is an edge of the graph 
        Throws:
        -ValueError if start or end are not vertices in the graph
        -ValueError if start end is not an edge of the graph
        
        Removes the edge START END from the graph.
        '''
        
        if not self.isEdge(start, end):
            raise ValueError("The Edge does not exist!")
        for index in range(len(self.__inMap[end])):
            edge = self.__inMap[end][index]
            if edge[0] == start:
                self.__inMap[end].pop(index)
                break;
        for index in range(len(self.__outMap[start])):
            edge = self.__outMap[start][index]
            if edge[0] == end:
                self.__outMap[start].pop(index)
                break;
        self.__no_edges -= 1
    
    def readFromFile(self, filename):
        '''
        Preconditions:
        -filename should be a valid, readable file
        Throws:
        -IOError if filename is not a valid, readable file
        -Unexpected Errors if the file does not have the below specified format
        
        Reads a Directed Graph from the FILE filename.
        The file must have the following format:
        no_vertcies no_edges
        start_vertex(1) end_vertex(1) cost(1)
        ...
        start_vertex(n-1) end_vertex(n-1) cost(n-1)
        '''
        
        file = open(filename, "r")
        file_string = file.readline()
        file_string = file_string.split(" ")
        self.__no_vertices = int(file_string[0])
        self.__no_edges = 0
        #no_edges will be incremented in every addEdge
        aux_edges = int(file_string[1])
        self.__inMap.clear()
        self.__outMap.clear()
        self.__vertices.clear()
        for index in range(self.__no_vertices):
            self.__inMap[index] = []
            self.__outMap[index] = []
            self.__vertices.append(index)
        for _ in range(aux_edges):
            file_string = file.readline()
            file_string = file_string.split(" ")
            start = int(file_string[0])
            end = int(file_string[1])
            cost = int(file_string[2])
            self.addEdge(start, end, cost)
        file.close()
    
    def __str__(self):
        '''
        Returns the graph codified as a string.
        '''
        
        result = ""
        result += str(self.getNoVertices()) + " " + str(self.getNoEdges()) + "\n"
        for vertex in self.getVertices():
            result += str(vertex) + " "
        result += "\n"
        
        #we have to display each edge only once
        #we know that an edge is memorized 2 times(once in inMap, and once in outMap), so we will display only outMap
        for vertex in self.getVertices():
            for edge in self.__outMap[vertex]:
                result += str(vertex) + " " + str(edge[0]) + " " + str(edge[1]) + "\n"
    
        return result
    
        
    def makeCopy(self):
        '''
        Returns a (deep) copy of the Directed Graph.
        '''
        
        new_graph = DirectedGraph(0)
        new_graph.__no_vertices = self.__no_vertices
        new_graph.__no_edges = self.__no_edges
        new_graph.__inMap = copy.deepcopy(self.__inMap)
        new_graph.__inMap = copy.deepcopy(self.__outMap)
        new_graph.__vertices = copy.deepcopy(self.__vertices)
        return new_graph
    
    
    @staticmethod
    def createRandomGraph(n, m):
        '''
        Returns a newly created Directed Graph with N nodes and M vertices, randomly generated.
        '''
        
        if (n * n < m):
            raise ValueError("The number of edges is too big!")
        new_graph = DirectedGraph(0)
        while n > 0:
            vertex = random.randrange(1000)
            if vertex not in new_graph.getVertices():
                new_graph.addVertex(vertex)
                n -= 1;
        n = new_graph.getNoVertices()
        possible_pairs = []
        for i in range(n):
            for j in range(n):
                    possible_pairs.append([i, j])
        random.shuffle(possible_pairs)
        while m > 0:
            m -= 1
            cost = random.randrange(2000) - 1000
            pair = possible_pairs.pop()
            start = pair[0]
            end = pair[1]
            new_graph.addEdge(new_graph.__vertices[start], new_graph.__vertices[end], cost)
        return new_graph
    
    def dijkstraBackwards(self, start, end):
        '''
        Preconditions:
        -start, end integers
        -start, end is a vertex from the graph
        -all costs are positive
        Postconditions:
        -returns RETURN_LISt, which is a list containing the cost of the minimum-path, respectively another list representing the path itself.
        -returns [-1, []] if there is no path between start and end
        
        Errors:
        -Throws ValueError if start or end are not found in the graph.
        
        Computes the minimum cost path from start to end, using Dijkstra's Algorithm, and the cost of this path.
        '''
        
        priority_queue = []
        dist = {}
        prev = {}
        found = False
        
        if end not in self.__vertices or start not in self.__vertices:
            raise ValueError("The START or/and END vertex is not found in the graph!")
        
        heapq.heappush(priority_queue, (0, end))
        dist[end] = 0
        prev[end] = -1
        while (len(priority_queue) > 0):
            current_processed = heapq.heappop(priority_queue)[1] #priority_queue is formed of 2-element tuples
            for neighbour in self.getInboundNeighbours(current_processed):
                if neighbour not in dist.keys():
                    prev[neighbour] = current_processed
                    dist[neighbour] = self.getEdgeCost(neighbour, current_processed) + dist[current_processed]
                    if neighbour == start:
                        found = True
                        break
                    heapq.heappush(priority_queue, (dist[neighbour], neighbour))
        
        if (found):
            path = []
            current_processed = start
            while current_processed != -1: #-1 is prev[end]
                path.append(current_processed)
                current_processed = prev[current_processed]
            return [dist[start], path]
        return [-1, []] #it means there is no path between start and end
    
    
    def topologicalSorting(self):
        '''
        Performs a topological sorting on the graph.
        
        If the graph is a DAG, it returns a list of the vertices sorted in topological order.
        Otherwise, it returns None.
        '''
        
        sortedList = []
        inDegreeDic = {}
        queue = []
        
        for vertex in self.getVertices():
            inDegreeDic[vertex] = self.getInDegree(vertex)
            if inDegreeDic[vertex] == 0:
                queue.append(vertex)
        
        while (len(queue) != 0):
            currentProcessed = queue.pop(0)
            sortedList.append(currentProcessed)
            for neighbour in self.getOutboundNeighbours(currentProcessed):
                inDegreeDic[neighbour] -= 1
                if inDegreeDic[neighbour] == 0:
                    queue.append(neighbour)
        
        if (len(sortedList) != self.getNoVertices()):
            return None
        return sortedList
    
    @staticmethod
    def sortCost(edge):
        return edge[2]
    
    @staticmethod
    def findParent(edge, parent):
        if (parent[edge] == edge):
            return edge
        parent[edge] = DirectedGraph.findParent(parent[edge], parent)
        return parent[edge]
    
    @staticmethod
    def uniteTree(edge1, edge2, parent, rang):
        parentEdge1 = DirectedGraph.findParent(edge1, parent)
        parentEdge2 = DirectedGraph.findParent(edge2, parent)
        
        if (rang[parentEdge1] > rang[parentEdge2]):
            aux = parentEdge1
            parentEdge1 = parentEdge2
            parentEdge2 = aux
        
        parent[parentEdge1] = parentEdge2
        rang[parentEdge2] += rang[parentEdge1]
            
        
    
    def kruskalAlgorithm(self):
        '''
        Computes the Minimum Spanning Tree(MST) and the sum of its edges' costs, using Kruskal's Algorithm.
        Output:
        -a list LST containing 2 elements: sum and edgesList; edgesList is a list of edges(startEdge, endEdge, costEdge)
        -if the MST cannot be formed, it returns only [-1, []]
        '''
        
        MSTsum = 0
        MSTedges = []
        rang = {}
        parent = {}
        
        #initializing of rang and parent
        for vertex in self.getVertices():
            rang[vertex] = vertex
            parent[vertex] = vertex
        
        #sortedEdges is the list of edges, sorted by cost
        sortedEdges = []
        for vertex in self.getVertices():
            for edge in self.__outMap[vertex]:
                sortedEdges.append([vertex, edge[0], edge[1]])
                
        sortedEdges.sort(key = DirectedGraph.sortCost)
        
        noAddedEdges = 0
        index = 0
        while noAddedEdges < self.getNoVertices() - 1 and index < self.getNoEdges(): #MST contains m - 1 edges
            edge = sortedEdges[index]
            index += 1
            edge1 = edge[0]
            edge2 = edge[1]
            parentEdge1 = DirectedGraph.findParent(edge1, parent)
            parentEdge2 = DirectedGraph.findParent(edge2, parent)
            if parentEdge1 != parentEdge2: #the 2 edges are in different "clouds"
                noAddedEdges += 1
                DirectedGraph.uniteTree(edge1, edge2, parent, rang)
                MSTsum += self.getEdgeCost(edge1, edge2)
                MSTedges.append(edge)
        
        #print(str(index) + " " + str(noAddedEdges))
        #print(MSTsum)
        #for edge in MSTedges:
            #print(str(edge[0]) + " " + str(edge[1]) + " " + str(edge[2]))
        
        if noAddedEdges < self.getNoVertices() - 1:#a MST could not be created
            return [-1, []]
        return [MSTsum, MSTedges]
        