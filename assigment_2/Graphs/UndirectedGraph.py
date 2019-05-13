'''
Created on May 6, 2019

@author: antoniu
'''

import copy

class UndirectedGraph:
    
    def __travel_dfs(self, vertex, visited, current_component):
        '''
        Auxiliary function used in Depth-First Search.
        '''
        
        current_component.append(vertex)
        for neighbour in self.getNeighbours(vertex):
            if neighbour not in visited:
                visited.add(neighbour)
                self.__travel_dfs(neighbour, visited, current_component)
    
    def getConnectedComponents(self):
        '''
        Returns a list whose elements are connected component. Each connected component is stores as a list of vertices, which are integers.
        '''
        
        visited = set()
        connected_components = list()
        for vertex in self.getVertices():
            if vertex not in visited:
                visited.add(vertex)
                current_component = list()
                self.__travel_dfs(vertex, visited, current_component)
                connected_components.append(current_component)
        return connected_components
    
    def __init__(self, no_vertices = 0):
        '''
        Preconditions:
        -No_Vertices is an integer
        -No_Vertices >= 0
        
        Creates an Undirected Graph with No_Vertices.
        Vertices have values between 0 and (No_Vertices - 1).
        '''
        self.__no_vertices = no_vertices
        self.__no_edges = 0
        self.__neighbours = {}
        self.__vertices = []
        for index in range(no_vertices):
            self.__neighours[index] = []
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
        -start, end is a vertex from the graph
        -there is no edge between start and end
        Throws:
        -ValueError if start or end are not vertices in the graph
        -ValueError if there is already an edge between start and end
        
        Adds an edge from vertex START to END with the cost COST.(COST is implicitly 0)
        '''
        
        if self.isEdge(start, end):
            raise ValueError("The Edge does already exist!")
        #if (start == end):
            #raise ValueError("We cannot have an edge with endpoints being the same vertex!")
        if (start in self.__vertices and end in self.__vertices):
            self.__neighbours[end].append([start, cost])
            self.__neighbours[start].append([end, cost])
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
            if end in self.getNeighbours(start):
                    return True
            return False
        else:
            raise ValueError("The Start Vertex or/and End Vertex does not exist!")
    
    def getDegree(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if there is no vertex VERTEX in the graph
        
        Returns the degree of the vertex.
        '''
        
        if vertex in self.__vertices:
            return len(self.__neighbours[vertex])
        else:
            raise ValueError("The Vertex does not exist!")
    
    def getNeighbours(self, vertex):
        '''
        Preconditions:
        -vertex integer
        -vertex is a vertex in the graph
        Throws:
        -ValueError if there is no vertex VERTEX in the graph
        
        Returns an iterator containing all the neighbours of vertex VERTEX.
        '''
        
        if vertex in self.__vertices:
            for edge in self.__neighbours[vertex]:
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
        for edge in self.__neighbours[start]:
            if edge[0] == end:
                edge[1] = cost
                break
        for edge in self.__neighbours[end]:
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
        for edge in self.__neighbours[start]:
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
        self.__neighbours[vertex] = []
    
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
        for index in range(len(self.__neighbours[end])):
            edge = self.__neighbours[end][index]
            if edge[0] == start:
                self.__neighbours[end].pop(index)
                break;
        for index in range(len(self.__neighbours[start])):
            edge = self.__neighbours[start][index]
            if edge[0] == end:
                self.__neighbours[start].pop(index)
                break;
        self.__no_edges -= 1
    
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
        
        #self.__neighbours is modified by the method removeEdge, so we have to save it prior to
        #iterating through the map
        neighboursAux = copy.deepcopy(self.__neighbours[vertex]) 
        for edge in neighboursAux:
            neighbour = edge[0]
            self.removeEdge(neighbour, vertex)
            
        self.__neighbours.pop(vertex)
        self.__no_vertices -= 1
        self.__vertices.remove(vertex)
    
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
        self.__neighbours.clear()
        self.__vertices.clear()
        for index in range(self.__no_vertices):
            self.__neighbours[index] = []
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
        for vertex in self.getVertices():
            for edge in self.__neighbours[vertex]:
                if (edge[0] >= vertex):
                    result += str(vertex) + " " + str(edge[0]) + " " + str(edge[1]) + "\n"
    
        return result
    
        
    def makeCopy(self):
        '''
        Returns a (deep) copy of the Undirected Graph.
        '''
        
        new_graph = UndirectedGraph(0)
        new_graph.__no_vertices = self.__no_vertices
        new_graph.__no_edges = self.__no_edges
        new_graph.__neighbours = copy.deepcopy(self.__neighbours)
        new_graph.__vertices = copy.deepcopy(self.__vertices)
        return new_graph
