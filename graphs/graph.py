"""
Simple graph implementation
"""
from utils import Stack, Queue


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError(
                f"Both {v1} and {v2} must be in the graph as vertices")

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
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
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])

        while queue.size():
            path = queue.dequeue()
            current_vert = path[-1]

            if current_vert == destination_vertex:
                return path

            if current_vert not in visited:
                visited.add(current_vert)

                for vertex in self.vertices[current_vert]:
                    new_path = list(path)
                    new_path.append(vertex)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


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
