'''
Created on Mar 18, 2019

@author: toni
'''

import unittest
from Graphs.DirectedGraph import DirectedGraph

class TestDirectedGraph(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def test_getNoVertices(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        assert graph.getNoVertices() == 10
        
        graph.addVertex(10)
        assert graph.getNoVertices() == 11
        
        graph.removeVertex(0)
        assert graph.getNoVertices() == 10
        
        graph.removeVertex(5)
        assert graph.getNoVertices() == 9

    def test_getNoEdges(self):
        graph = DirectedGraph(10)
        
        assert graph.getNoEdges() == 0
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        assert graph.getNoEdges() == 3
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        assert graph.getNoEdges() == 5
        
        graph.removeEdge(0, 3)
        
        assert graph.getNoEdges() == 4
        
        graph.addEdge(6, 4)
        
        assert graph.getNoEdges() == 5
    
    def test_getVertices(self):
        graph = DirectedGraph(10)
        count = 0
        
        graph.addVertex(10)
        
        for vertex in graph.getVertices():
            assert vertex == count
            count += 1
    
    def test_addEdge(self):
        #test copied from test_isEdge
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        assert graph.isEdge(0, 1) == True
        assert graph.isEdge(0, 2) == True
        assert graph.isEdge(0, 3) == True 
        assert graph.isEdge(1, 0) == True
        assert graph.isEdge(1, 9) == True
        
        assert graph.isEdge(2, 0) == False
        assert graph.isEdge(3, 0) == False 
        assert graph.isEdge(9, 1) == False
        
        try:
            graph.isEdge(-1, 0)
            assert False
        except ValueError:
            pass
        
        try:
            graph.isEdge(2, 10)
            assert False
        except ValueError:
            pass
    
    def test_isEdge(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        assert graph.isEdge(0, 1) == True
        assert graph.isEdge(0, 2) == True
        assert graph.isEdge(0, 3) == True 
        assert graph.isEdge(1, 0) == True
        assert graph.isEdge(1, 9) == True
        
        assert graph.isEdge(2, 0) == False
        assert graph.isEdge(3, 0) == False 
        assert graph.isEdge(9, 1) == False
        
        try:
            graph.isEdge(-1, 0)
            assert False
        except ValueError:
            pass
        
        try:
            graph.isEdge(2, 10)
            assert False
        except ValueError:
            pass
    
    def test_getInDegree(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        assert graph.getInDegree(0) == 1
        assert graph.getInDegree(1) == 1
        assert graph.getInDegree(2) == 1
        assert graph.getInDegree(3) == 1
        assert graph.getInDegree(9) == 1
        assert graph.getInDegree(4) == 0
        
        try:
            graph.getInDegree(10)
            assert False
        except ValueError:
            pass
    
    def test_outInDegree(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        assert graph.getOutDegree(0) == 3
        assert graph.getOutDegree(1) == 2
        assert graph.getOutDegree(2) == 0
        assert graph.getOutDegree(3) == 0
        assert graph.getOutDegree(9) == 0
        assert graph.getOutDegree(4) == 0
        
        try:
            graph.getInDegree(10)
            assert False
        except ValueError:
            pass
    
    def test_getOutboundNeighbours(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 0)
        graph.addEdge(0, 2, 0)
        graph.addEdge(0, 3, 0)
        graph.addEdge(1, 0, 0)
        graph.addEdge(1, 9, 0)
        
        result_lst = [1, 2, 3]
        aux_lst = []
        for neighbour in graph.getOutboundNeighbours(0):
            aux_lst.append(neighbour)
        assert result_lst == aux_lst
        
        result_lst = [0, 9]
        aux_lst = []
        for neighbour in graph.getOutboundNeighbours(1):
            aux_lst.append(neighbour)
        assert result_lst == aux_lst
        
        result_lst = []
        aux_lst = []
        for neighbour in graph.getOutboundNeighbours(2):
            aux_lst.append(neighbour)
        assert result_lst == aux_lst
    
    def test_getEdgeCost(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 2)
        graph.addEdge(0, 2, 3)
        graph.addEdge(0, 3, 4)
        graph.addEdge(1, 0, 5)
        graph.addEdge(1, 9, 6)
        
        assert graph.getEdgeCost(0, 1) == 2
        assert graph.getEdgeCost(0, 2) == 3
        assert graph.getEdgeCost(0, 3) == 4
        assert graph.getEdgeCost(1, 0) == 5
        assert graph.getEdgeCost(1, 9) == 6
        
        try:
            graph.getEdgeCost(0, 4)
            assert False
        except ValueError:
            pass
    
    def test_modifyCost(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 2)
        graph.addEdge(0, 2, 3)
        graph.addEdge(0, 3, 4)
        graph.addEdge(1, 0, 5)
        graph.addEdge(1, 9, 6)
        
        graph.modifyCost(0, 1, 7)
        graph.modifyCost(1, 9, 3)
        graph.modifyCost(0, 3, 4)
        
        assert graph.getEdgeCost(0, 1) == 7
        assert graph.getEdgeCost(0, 2) == 3
        assert graph.getEdgeCost(0, 3) == 4
        assert graph.getEdgeCost(1, 0) == 5
        assert graph.getEdgeCost(1, 9) == 3
        
        try:
            graph.modifyCost(0, 4, 10)
            assert False
        except ValueError:
            pass
    
    def test_removeVertex(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 2)
        graph.addEdge(0, 2, 3)
        graph.addEdge(0, 3, 4)
        graph.addEdge(1, 0, 5)
        graph.addEdge(4, 0, 5)
        graph.addEdge(1, 9, 6)
        
        graph.removeVertex(0)
        assert graph.getNoVertices() == 9
        assert graph.getNoEdges() == 1, graph.getNoEdges()
        assert 0 not in graph.getVertices()
        assert graph.getInDegree(1) == 0
        assert graph.getOutDegree(1) == 1
    
    def test_removeEdge(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 2)
        graph.addEdge(0, 2, 3)
        graph.addEdge(0, 3, 4)
        graph.addEdge(1, 0, 5)
        graph.addEdge(1, 9, 6)
        
        graph.removeEdge(0, 3)
        assert graph.isEdge(0, 3) == False
        assert graph.getNoEdges() == 4
        
        graph.removeEdge(1, 0)
        assert graph.isEdge(1, 0) == False
        assert graph.getNoEdges() == 3
        
        try:
            graph.removeEdge(0, 3)
            assert False
        except ValueError:
            pass
        
        try:
            graph.removeEdge(4, 5)
            assert False
        except ValueError:
            pass
    
    def test_addVertex(self):
        graph = DirectedGraph(10)
        
        graph.addVertex(10)
        if not 10 in graph.getVertices():
            assert False
        if 11 in graph.getVertices():
            assert False
    
    def test_str(self):
        graph = DirectedGraph(10)
        
        graph.addEdge(0, 1, 2)
        graph.addEdge(0, 2, 3)
        graph.addEdge(0, 3, 4)
        graph.addEdge(1, 0, 5)
        graph.addEdge(1, 9, 6)
        
        graph_string = str(graph)
        correct_string = "10 5\n0 1 2 3 4 5 6 7 8 9 \n0 1 2\n0 2 3\n0 3 4\n1 0 5\n1 9 6\n"
        assert graph_string == correct_string, graph_string