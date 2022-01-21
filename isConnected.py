"""
    create a function that returns True if vertex i and vertex j
    are connected in the graph represented by the input adjacency matrix A
"""

import numpy as np


def isConnected(A: np.array, i: int, j: int) -> bool:

    paths = A       # initialize the paths matrix to adjacency matrix A
    number_vertices = A.shape[0]    # find the number of vertices in the graph
    number_edges = np.sum(A) / 2    # find the number of edges in the graph

    # if node vi and vj are adjacent, return True
    if paths[i-1][j-1] > 0:
        print(f'Vertex {i} and vertex {j} are adjacent.')
        return True

    else:
        # run the loop until we find a path
        for pathLength in range(2, number_vertices):
            paths = np.dot(paths, A)        # exponentiate the adjacency matrix
            if paths[i - 1][j - 1] > 0:
                print(f'There is a path with {pathLength} edges from vertex {i} to vertex {j}.')
                return True
            # found no paths, the vertices are not connected
            if pathLength == number_edges:
                print(f'There are no paths from vertex {i} to vertex {j}.')
                return False


def main():
    A1 = np.array([[0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1],
                   [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0],
                   [1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0]])
    print(isConnected(A1, 1, 4))
    print(isConnected(A1, 2, 3))
    print(isConnected(A1, 5, 6))

    A2 = np.array([[0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
                   [0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0],
                   [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0]])
    print(isConnected(A2, 1, 6))
    print(isConnected(A2, 2, 5))
    print(isConnected(A2, 1, 4))


"""main()      # test the code"""
