'''
Created on Mar 19, 2019

@author: antoniu
'''

class Console:
    
    def __init__(self, controller):
        self.__controller = controller
    
    @staticmethod
    def printCommands():
        print("\nRead from file: read filename")
        print("Print graph: print")
        print("Get number of edges: get-no-edges")
        print("Get number of vertices: get-no-vertices")
        print("Get a list of vertices: get-vertices")
        print("Find out if there is an edge between 2 vertices: is-edge START-VERTEX END-VERTEX")
        print("Get the degree of a vertex: degree VERTEX")
        print("Get a list of neighbours for a vertex: vertices VERTEX")
        print("Modify cost of an edge: update START-VERTEX END_VERTEX NEW-COST")
        print("Add a new vertex: add-vertex VERTEX")
        print("Remove a vertex: remove-vertex VERTEX")
        print("Add a new edge: add-edge START-VERTEX END-VERTEX COST")
        print("Remove an edge: remove-edge START-VERTEX END-VERTEX")
        print("Print the connected components using DFS: DFS")
        print("Exit: exit\n")
    
    def __ui_readFromFile(self, commands):
        self.__controller.readFromFile(commands)
    
    def __ui_print(self):
        print (self.__controller.toString())
    
    def __ui_getNoEdges(self):
        print(self.__controller.getNoEdges())
    
    def __ui_getNoVertices(self):
        print(self.__controller.getNoVertices())
    
    def __ui_getVertices(self):
        output = ""
        vertices_list = self.__controller.getVertices()
        for vertex in vertices_list:
            output += str(vertex) + " "
        print(output)
    
    def __ui_isEdge(self, commands):
        start_vertex = 0
        end_vertex = 0
        try:
            start_vertex = int(commands[1])
            end_vertex = int(commands[2])
        except:
            print("The Start-Vertex or End-Vertex is not a valid integer!")
            return
        try:
            cost = self.__controller.getEdgeCost(start_vertex, end_vertex)
        except ValueError as ve:
            print (str(ve))
            return
        print ("There is an edge between " + str(start_vertex) + " and " + str(end_vertex) + " with cost " + str(cost) + ".")
    
    def __ui_getDegree(self, commands):
        vertex = 0
        try:
            vertex = int(commands[1])
        except:
            print("The Vertex is not a valid integer!")
            return
        try:
            print (self.__controller.getDegree(vertex))
        except ValueError as ve:
            print (str(ve))
            return
    
    def __ui_getNeighbours(self, commands):
        vertex = 0
        lst = []
        output = ""
        try:
            vertex = int(commands[1])
        except:
            print("The Vertex is not a valid integer!")
            return
        try:
            lst = self.__controller.getNeighbours(vertex)
        except ValueError as ve:
            print (str(ve))
            return
        for vertex in lst:
            output += str(vertex) + " "
        print (output)
    
    def __ui_modifyCost(self, commands):
        start_vertex = 0
        end_vertex = 0
        cost = 0
        try:
            start_vertex = int(commands[1])
            end_vertex = int(commands[2])
            cost = int(commands[3])
        except:
            print("The Start Vertex, End Vertex or New Cost is not a valid integer!")
            return
        try:
            self.__controller.modifyCost(start_vertex, end_vertex, cost)
        except ValueError as ve:
            print (str(ve))
            return
        print("Update successful!")
    
    def __ui_addVertex(self, commands):
        vertex = 0
        try:
            vertex = int(commands[1])
        except:
            print("The Vertex is not a valid integer!")
            return
        try:
            self.__controller.addVertex(vertex)
        except ValueError as ve:
            print (str(ve))
            return
        print("Vertex added successfully!")
    
    def __ui_removeVertex(self, commands):
        vertex = 0
        try:
            vertex = int(commands[1])
        except:
            print("The Vertex is not a valid integer!")
            return
        try:
            self.__controller.removeVertex(vertex)
        except ValueError as ve:
            print (str(ve))
            return
        print("Vertex removed successfully!")
    
    def __ui_addEdge(self, commands):
        start_vertex = 0
        end_vertex = 0
        cost = 0
        try:
            start_vertex = int(commands[1])
            end_vertex = int(commands[2])
            cost = int(commands[3])
        except:
            print("The Start Vertex, End Vertex or New Cost is not a valid integer!")
            return
        try:
            self.__controller.addEdge(start_vertex, end_vertex, cost)
        except ValueError as ve:
            print (str(ve))
            return
        print("Edge added successfully!")
    
    def __ui_removeEdge(self, commands):
        start_vertex = 0
        end_vertex = 0
        try:
            start_vertex = int(commands[1])
            end_vertex = int(commands[2])
        except:
            print("The Start Vertex or End Vertex is not a valid integer!")
            return
        try:
            self.__controller.removeEdge(start_vertex, end_vertex)
        except ValueError as ve:
            print (str(ve))
            return
        print("Edge removed successfully!")
    
    def __ui_dfs(self):
        list_of_components = self.__controller.getConnectedComponents()
        for component in list_of_components:
            component_string = ""
            for vertex in component:
                component_string += str(vertex) + " "
            print(component_string)
    
    def run(self):
        while True:
            Console.printCommands()
            commands = input("Insert commands: ").split(" ")
            if commands[0] == "read" and len(commands) == 2:
                self.__ui_readFromFile(commands)
            elif commands[0] == "print" and len(commands) == 1:
                self.__ui_print()
            elif commands[0] == "get-no-edges" and len(commands) == 1:
                self.__ui_getNoEdges()
            elif commands[0] == "get-no-vertices" and len(commands) == 1:
                self.__ui_getNoVertices()
            elif commands[0] == "get-vertices" and len(commands) == 1:
                self.__ui_getVertices()
            elif commands[0] == "is-edge" and len(commands) == 3:
                self.__ui_isEdge(commands)
            elif commands[0] == "degree" and len(commands) == 2:
                self.__ui_getDegree(commands)
            elif commands[0] == "vertices" and len(commands) == 2:
                self.__ui_getNeighbours(commands)
            elif commands[0] == "update" and len(commands) == 4:
                self.__ui_modifyCost(commands)
            elif commands[0] == "add-vertex" and len(commands) == 2:
                self.__ui_addVertex(commands)
            elif commands[0] == "remove-vertex" and len(commands) == 2:
                self.__ui_removeVertex(commands)
            elif commands[0] == "add-edge" and len(commands) == 4:
                self.__ui_addEdge(commands)
            elif commands[0] == "remove-edge" and len(commands) == 3:
                self.__ui_removeEdge(commands)
            elif (commands[0] == "DFS" or commands[0] == "dfs") and len(commands) == 1:
                self.__ui_dfs()
            elif commands[0] == "exit" and len(commands) == 1:
                return
            else:
                print("Invalid command!\n")