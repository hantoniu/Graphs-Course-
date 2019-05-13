'''
Created on Mar 18, 2019

@author: toni
'''

from Graphs.UndirectedGraph import UndirectedGraph
from Controller.Controller import Controller
from Console.Console import Console

graph = UndirectedGraph()
controller = Controller(graph)
console = Console(controller)
console.run()