from enum import Enum
from Shape import *


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class Vertex:
    def __init__(self, shape: Shape, color: Color):
        self.shape = shape
        self.color = color
        self.group = []


def create_vertices(shapes, states):
    vertices = []
    i = 0
    for letter in shapes:
        if letter != '/':
            vertices.append(Vertex(letter_to_shape(letter)(states[i]), Color.WHITE))
            i += 1
    return vertices


class ShapesDFS:
    def __init__(self, shapes, states, size):
        self.size = size
        self.vertices = create_vertices(shapes, states)
        self.groups = 0
        self.out_of_bounds = 0

    def DFS(self):
        for i, vertex in enumerate(self.vertices):
            if vertex.color == Color.WHITE:
                self.groups += 1  # for now we only need this. TODO decide if deleting the group attribute
                self.DFS_visit(vertex, i)

    # TODO- for now we only need number of groups
    def DFS_visit(self, u, i):
        u.color = Color.GRAY
        for pos in u.shape.go_to(i, self.size):
            if pos is None:
                self.out_of_bounds += 1
            else:
                v = self.vertices[pos]  # v in adj(v)
                # check if v hasn't been visited & v an u reaches each other
                if v.color == Color.WHITE and i in v.shape.go_to(pos, self.size):
                    u.group.append(v)
                    v.group.append(u)
                    self.DFS_visit(v, pos)
        u.color = Color.BLACK


def dfs_test():
    board_shapes = 'LTLi/iiTL/LTTi/iLli'
    optimal_solution = [3, 0, 2, 0, 2, 2, 1, 1, 3, 0, 2, 3, 2, 0, 1, 3]
    dfs = ShapesDFS(board_shapes, optimal_solution, 4)
    dfs.DFS()
    print(dfs.groups)
    print(dfs.out_of_bounds)


dfs_test()