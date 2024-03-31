class Boards:
    def __init__(self, size):
        self.size = size
        self.current = [0 for _ in range(size*size)]
        if size == 4:
            self.shapes = 'LTLi/iiTL/LTTi/iLli'
            self.optimal = [3, 0, 2, 0,
                            2, 2, 1, 1,
                            3, 0, 2, 3,
                            2, 0, 1, 3]
        elif size == 5:
            self.shapes = 'iTlii/LTLlL/iTLLL/iTTLi/LLLli'
            self.optimal = [1, 0, 1, 3, 0,
                            3, 3, 3, 1, 1,
                            2, 1, 1, 3, 2,
                            0, 1, 0, 1, 2,
                            0, 1, 0, 1, 3]
        elif size == 7:
            self.shapes = 'iiLliLL/TLliili/LTTlTTi/LTiTTli/iTTTLii/iTliTTT/iLLLLii'
            self.optimal = [0, 0, 3, 1, 3, 3, 2,
                            1, 1, 0, 0, 0, 0, 2,
                            0, 0, 3, 0, 1, 2, 3,
                            3, 3, 2, 1, 2, 1, 3,
                            2, 1, 0, 2, 2, 0, 0,
                            1, 3, 0, 0, 1, 2, 3,
                            1, 1, 0, 1, 0, 3, 2]
        elif size == 10:
            self.shapes = ('LTTlTlliiL/lliiTiilTL/iiiLTLiLTi/iiTTiiTLli/TiLTTlLLTT/TllLTTlTLl/iiiTlTTLli/LTLTLiiiii'
                           '/iiTTLLLiil/iTLiTLLTTL')
            self.optimal = [3, 0, 0, 1, 0, 1, 1, 3, 1, 2,
                            0, 0, 2, 1, 3, 0, 1, 1, 0, 1,
                            2, 2, 0, 3, 2, 1, 1, 2, 1, 3,
                            0, 1, 3, 1, 3, 1, 0, 1, 0, 0,
                            1, 3, 0, 2, 0, 1, 1, 3, 2, 3,
                            1, 1, 1, 2, 1, 0, 1, 2, 2, 0,
                            2, 0, 1, 3, 0, 1, 0, 2, 0, 2,
                            3, 2, 2, 1, 1, 2, 2, 2, 2, 0,
                            2, 0, 1, 2, 2, 3, 2, 0, 0, 0,
                            1, 2, 1, 1, 2, 1, 0, 2, 2, 1
                            ]
        else:
            self.shapes = 'Error- Invalid size'
            self.optimal = []

    def reset_board(self):
        self.current = [0 for _ in range(self.size*self.size)]
