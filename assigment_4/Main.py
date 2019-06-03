'''
Created on Mar 18, 2019

@author: toni
'''

from DirectedGraph.DirectedGraph import DirectedGraph
from Controller.Controller import Controller
from Console.Console import Console

graph = DirectedGraph()
controller = Controller(graph)
console = Console(controller)
console.run()