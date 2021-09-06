#  File: TopoSort.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/25/21
#  Date Last Modified: 4/30/21

import sys


#Copied the code from the lecture
class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def __str__(self):
        return str(self.stack)


#Copied the code from the lecture
class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

    #return first value
    def peek(self):
        return self.queue[0]


#Copied the code from the lecture
class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.get_label())


class Graph(object):
  #Code copied from A20
    #Constructor
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    #Code copied from A20
    # check if a vertex is already in the graph
    def has_vertex(self, label):
        num_vert = len(self.Vertices)
        for i in range(num_vert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    #Code copied from A20
    # given the label get the index of a vertex
    def get_index(self, label):
        num_vert = len(self.Vertices)
        for i in range(num_vert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    #Code copied from A20
    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        num_vert = len(self.Vertices)
        for i in range(num_vert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(num_vert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight


    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_vertex(self, v):
        num_vert = len(self.Vertices)
        for i in range(num_vert):
            if self.adjMat[v][i] > 0:
                return i
        return -1

    # modified dfs; aka the has_cycle helper function
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        theStack.push(v)

        # visit all the other vertices according to depth
        prev = -1
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_vertex(theStack.peek())

            #If you have already visited it pop if from the stack
            if u == -1:
                u = theStack.pop()

            #if in path and you have come back to it it must create a cycle
            elif u == v:
                return True

            #Else keep traversing through the stack
            else:
                #Check to see if you reach the end of the stack
                if theStack.size() >= len(self.Vertices):
                    return False
                #Else keep traversing through the stack
                else:
                    lst = str(theStack)
                    if u == prev:
                        return False
                    prev = u
                    theStack.push(u)

        # the stack is empty, let us rest the flags
        num_vert = len(self.Vertices)
        for i in range(num_vert):
            (self.Vertices[i]).visited = False

    # do a depth first search in a graph
    def has_cycle(self):
        num_vert = len(self.Vertices)
        for i in range(num_vert):
            if self.dfs(i):
                return True
        return False


    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        idx = self.get_index(vertexLabel)
        num_vert = len(self.Vertices)
        for i in range(num_vert):
            self.adjMat[i].pop(idx)
        self.adjMat.pop(idx)
        self.Vertices.pop(idx)

    # Finds the vertices with no in_vertices
    def toposort(self):
        #Ceate an empty list
        lst = []
        #loop while the length of the adjMat > 0
        while len(self.adjMat) > 0:
            #Create and empty temp list
            temp = []
            #for loop over the number of vertices
            for to_vert in range(len(self.Vertices)):
                #Have a counter variable
                count = 0

                for from_vert in range(len(self.Vertices)):
                    if self.adjMat[from_vert][to_vert] != 0:
                        count += 1
                  
                if count == 0:
                    letter = self.Vertices[to_vert].get_label()
                    lst.append(letter)
                    temp.append(letter)
            #
            for item in temp:
                self.delete_vertex(item)
        return lst

def main():
    # create the Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        graph = line.strip()
        if i == 0:
            start_str = graph
        theGraph.add_vertex(graph)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = ord(str(edge[0])) - ord(start_str)
        finish = ord(str(edge[1])) - ord(start_str)
        theGraph.add_directed_edge(start, finish)



    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)

if __name__ == "__main__":
    main()