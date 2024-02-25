from abc import abstractmethod


def matrix_to_vector_pos(pos, size):
    if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
        return None
    return pos[1] * size + pos[0]


def vector_to_matrix_pos(pos, size):
    if pos < 0 or pos >= size:
        return None
    return pos % size, pos // size


class Shape:
    def __init__(self, state):
        self.state = state

    def go_to(self, pos, size):
        (x, y) = vector_to_matrix_pos(pos, size)
        return [matrix_to_vector_pos(pos, size) for pos in self.go_to_pos(x, y)]

    @abstractmethod
    def go_to_pos(self, x, y):
        pass


class L_shape(Shape):
    def go_to_pos(self, x, y):
        if self.state == 0:
            return [(x, y - 1), (x + 1, y)]
        elif self.state == 1:
            return [(x - 1, y), (x, y - 1)]
        elif self.state == 2:
            return [(x - 1, y), (x, y + 1)]
        else:
            return [(x, y + 1), (x + 1, y)]


class T_shape(Shape):
    def go_to_pos(self, x, y):
        if self.state == 0:
            return [(x - 1, y), (x + 1, y), (x, y + 1)]
        elif self.state == 1:
            return [(x, y - 1), (x, y + 1), (x + 1, y)]
        elif self.state == 2:
            return [(x - 1, y), (x + 1, y), (x, y - 1)]
        else:
            return [(x - 1, y), (x, y - 1), (x, y + 1)]


class i_shape(Shape):
    def go_to_pos(self, x, y):
        if self.state == 0:
            return [(x, y + 1)]
        elif self.state == 1:
            return [(x + 1, y)]
        elif self.state == 2:
            return [(x, y - 1)]
        else:
            return [(x - 1, y)]


class l_shape(Shape):
    def go_to_pos(self, x, y):
        if self.state == 0 or self.state == 2:
            return [(x, y - 1), (x, y + 1)]
        else:
            return [(x - 1, y), (x + 1, y)]
