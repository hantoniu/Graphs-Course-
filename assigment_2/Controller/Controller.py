'''
Created on Mar 19, 2019

@author: antoniu
'''

class Controller:
    
    def __init__(self, graph):
        self.__graph = graph
        self.__graph.readFromFile("graph.txt") #we read from file automatically
    
    def readFromFile(self, commands):
        self.__graph.readFromFile(commands[1])
    
    def toString(self):
        return str(self.__graph)
    
    def getNoEdges(self):
        return self.__graph.getNoEdges()
    
    def getNoVertices(self):
        return self.__graph.getNoVertices()
    
    def getVertices(self):
        vertices_list = []
        for vertex in self.__graph.getVertices():
            vertices_list.append(vertex)
        return vertices_list
    
    def getEdgeCost(self, start_vertex, end_vertex):
        return self.__graph.getEdgeCost(start_vertex, end_vertex)
    
    def getDegree(self, vertex):
        return self.__graph.getDegree(vertex)
    
    def getNeighbours(self, vertex):
        lst = []
        for vertex in self.__graph.getNeighbours(vertex):
            lst.append(vertex)
        return lst
    
    def modifyCost(self, start_vertex, end_vertex, cost):
        self.__graph.modifyCost(start_vertex, end_vertex, cost)
    
    def addVertex(self, vertex):
        self.__graph.addVertex(vertex)
    
    def removeVertex(self, vertex):
        self.__graph.removeVertex(vertex)
    
    def addEdge(self, start_vertex, end_vertex, cost):
        self.__graph.addEdge(start_vertex, end_vertex, cost)
    
    def removeEdge(self, start_vertex, end_vertex):
        self.__graph.removeEdge(start_vertex, end_vertex)
    
    def getConnectedComponents(self):
        return self.__graph.getConnectedComponents()
            