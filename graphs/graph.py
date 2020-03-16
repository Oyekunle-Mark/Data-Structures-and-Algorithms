"""
Simple graph implementation
"""
from typing import TypeVar, Generic, Set
from utils import Stack, Queue

T = TypeVar('T')


class Graph(Generic[T]):

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id: T) -> None:
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1: T, v2: T) -> None:
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError(
                f"Both {v1} and {v2} must be in the graph as vertices")

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id) -> Set[T]:
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            raise IndexError(f"Cannot find {vertex_id} in the graph")

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # keep track of visited vertices
        visited = set()
        # create a queue class
        queue = Queue()
        # enqueue the starting vertex
        queue.enqueue(starting_vertex)

        # while queue is not empty
        while queue.size():
            # dequeue the queue
            current_vertex = queue.dequeue()

            # if current vertex has not been visited
            if current_vertex not in visited:
                # add ti to visited
                visited.add(current_vertex)
                # print the current vertex
                print(current_vertex)

                # for every neighbors of current_vertex
                for vertex in self.vertices[current_vertex]:
                    # add it to the queue
                    queue.enqueue(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # keep track of visited vertices
        visited = set()
        # create a stack class
        stack = Stack()
        # push the starting vertex onto the stack
        stack.push(starting_vertex)

        # while stack is not empty
        while stack.size():
            # pop from the stack
            current_vertex = stack.pop()

            # if current vertex has not been visited
            if current_vertex not in visited:
                # add it to visited
                visited.add(current_vertex)
                # print the current vertex
                print(current_vertex)

                # for every neighbors of current_vertex
                for vertex in self.vertices[current_vertex]:
                    # push it onto the stack
                    stack.push(vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if visited is not set
        if visited is None:
            # set it to empty set
            visited = set()

        # add current vertex to visited
        visited.add(starting_vertex)
        # print the vertex
        print(starting_vertex)

        # for every neighbors of current vertex
        for vertex in self.vertices[starting_vertex]:
            # if not visited already
            if vertex not in visited:
                # recursively call dft passing in the visited set
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create the queue class
        queue = Queue()
        # would hold the visited vertices
        visited = set()
        # add the starting vertex as a list of vert
        queue.enqueue([starting_vertex])

        # while the queue is not empty
        while queue.size():
            # dequeue a path from the queue
            path = queue.dequeue()
            # get the last vertex from the path
            current_vert = path[-1]

            # if the current_vert is teh destination vert
            if current_vert == destination_vertex:
                # return the path
                return path

            # if current_vert has not been visited
            if current_vert not in visited:
                # add it to visited
                visited.add(current_vert)

                # for every neighbors of current_vert
                for vertex in self.vertices[current_vert]:
                    # create a copy of the path
                    new_path = list(path)
                    # add the current vertex to the new path
                    new_path.append(vertex)
                    # enqueue the new_path onto the queue
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create the stack class
        stack = Stack()
        # would keep track of visited vertices
        visited = set()
        # push the starting vertex as a list of vert
        stack.push([starting_vertex])

        # while stack is not empty
        while stack.size():
            # pop a path from the stack
            path = stack.pop()
            # get the last vertex from the stack
            current_vert = path[-1]

            # if current_vert is the destination_vertex
            if current_vert == destination_vertex:
                # return path
                return path

            # if current_vert is not in visited:
            if current_vert not in visited:
                # add it to visited
                visited.add(current_vert)

                # for every neighbors of of current_vert
                for vertex in self.vertices[current_vert]:
                    # create a copy of the path
                    new_path = list(path)
                    # append the current vertex
                    new_path.append(vertex)
                    # push the new path onto the stack
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # would hold the found path to destination_vertex
        correct_path = []
        # holds the visited vertices
        visited = set()
        # initialize the stack class
        stack = Stack()
        # push the starting_vertex as a list
        stack.push([starting_vertex])

        # the inner recursive function
        def inner_dfs_recursive(starting_vertex, destination_vertex):
            # pops off a path from the stack
            path = stack.pop()
            # picks the last vertex from the path
            current_vert = path[-1]

            # base case of current_vert is the destination_vertex
            if current_vert == destination_vertex:
                # assess the nonlocal correct_path
                nonlocal correct_path
                # point correct_path to the path
                correct_path = path
                # return from the recursive function
                return

            # for neighbors of current_vert
            for vertex in self.vertices[current_vert]:
                # if vertex has not been visited
                if vertex not in visited:
                    # add it to visited visited
                    visited.add(vertex)
                    # create a copy of path
                    new_path = list(path)
                    # append the vert to the new path
                    new_path.append(vertex)
                    # push the new path onto the stack
                    stack.push(new_path)

                    # recursively call inner_dfs_recursive with vertex as the starting_vertex
                    inner_dfs_recursive(vertex, destination_vertex)

        # call the recursive function
        inner_dfs_recursive(starting_vertex, destination_vertex)

        # return the path
        return correct_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
