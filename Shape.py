from abc import abstractmethod


class Shape:
    def __init__(self, state):
        self.state = state

    def go_to(self, pos, size):
        (row, col) = vector_to_matrix_pos(pos, size)
        return [matrix_to_vector_pos(pos, size) for pos in self.go_to_pos(row, col)]

    @abstractmethod
    def go_to_pos(self, x, y):
        pass


class L_shape(Shape):
    def go_to_pos(self, row, col):
        if self.state == 0:
            return [(row - 1, col), (row, col + 1)]
        elif self.state == 1:
            return [(row - 1, col), (row, col - 1)]
        elif self.state == 2:
            return [(row + 1, col), (row, col - 1)]
        else:
            return [(row, col + 1), (row + 1, col)]

    def __str__(self):
        return f"L({self.state})"


class T_shape(Shape):
    def go_to_pos(self, row, col):
        if self.state == 0:
            return [(row, col - 1), (row, col + 1), (row + 1, col)]
        elif self.state == 1:
            return [(row - 1, col), (row + 1, col), (row, col + 1)]
        elif self.state == 2:
            return [(row, col - 1), (row - 1, col), (row, col + 1)]
        else:
            return [(row, col - 1), (row - 1, col), (row + 1, col)]

    def __str__(self):
        return f"T({self.state})"


class i_shape(Shape):
    def go_to_pos(self, row, col):
        if self.state == 0:
            return [(row + 1, col)]
        elif self.state == 1:
            return [(row, col + 1)]
        elif self.state == 2:
            return [(row - 1, col)]
        else:
            return [(row, col - 1)]

    def __str__(self):
        return f"i({self.state})"


class l_shape(Shape):
    def go_to_pos(self, row, col):
        if self.state == 0 or self.state == 2:
            return [(row - 1, col), (row + 1, col)]
        else:
            return [(row, col - 1), (row, col + 1)]

    def __str__(self):
        return f"l({self.state})"


def shape_go_to(letter, state, row, col):
    return letter_to_shape(letter)(state).go_to_pos(row - 1, col)


def matrix_to_vector_pos(pos, size):
    if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
        return None
    return pos[0] * size + pos[1]


def vector_to_matrix_pos(pos, size):
    return pos // size, pos % size


def create_shapes_matrix(shapes, states):
    matrix = []
    i = 0
    line = []
    for letter in shapes:
        if letter == '/':
            matrix.append(line)
            line = []
        else:
            line.append(letter_to_shape(letter)(states[i]))
            i += 1
    matrix.append(line)
    return matrix


def letter_to_shape(letter):
    if letter == 'L':
        return L_shape
    elif letter == 'T':
        return T_shape
    elif letter == 'i':
        return i_shape
    else:  # letter- 'l'
        return l_shape


def matrix_test():
    board_shapes = 'LTLi/iiTL/LTTi/iLli'
    optimal_solution = [3, 0, 2, 0, 2, 2, 1, 1, 3, 0, 2, 3, 2, 0, 1, 3]
    board = create_shapes_matrix(board_shapes, optimal_solution)
    s = ", "
    for line in board:
        print(f"[{s.join([str(s) for s in line])}]")


def print_shapes_matrix(shapes, solution):
    board = create_shapes_matrix(shapes, solution)
    s = ", "
    for line in board:
        print(f"[{s.join([str(s) for s in line])}]")


if __name__ == "__main__":
    matrix_test()
