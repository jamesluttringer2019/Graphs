"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v in visited:
                pass
            else:
                for i in self.get_neighbors(v):
                    q.enqueue(i)
                visited.add(v)
                print(v)
                
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = [starting_vertex]
        visited = set()
        
        while s != []:
            v = s.pop()
            
            if v in visited:
                pass
            else:
                for i in self.get_neighbors(v):
                    s.append(i)
                visited.add(v)
                print(v)


    def dft_recursive(self, starting_vertex, v=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in v:
            return None

        v.add(starting_vertex)
        print(starting_vertex)
        for i in self.get_neighbors(starting_vertex):
            return self.dft_recursive(i, v)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        s = [[starting_vertex]]
        visited = set()
        paths = []
    
        while s != []:
            p = s.pop()
            curr = p[-1]
            if curr == destination_vertex:
                paths.append(p)

            if curr not in visited:
                for i in self.get_neighbors(curr):
                    s.append(p+[i])

            visited.add(curr)

        shortest = paths[0]
        for p in paths:
            if len(p) < len(shortest):
                shortest = p
        return shortest

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        q = Queue()
        visited = set()
        paths = []

        q.enqueue([starting_vertex])
        while q.size()>0:
            p = q.dequeue()
            curr = p[-1]
            if curr == destination_vertex:
                paths.append(p)

            if curr not in visited:
                for i in self.get_neighbors(curr):
                    q.enqueue(p+[i])

            visited.add(curr)

        shortest = paths[0]
        for p in paths:
            if len(p) < len(shortest):
                shortest = p

        return shortest

    def dfs_recursive(self, starting_vertex, destination_vertex, path):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            return path.append(starting_vertex)
        


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
