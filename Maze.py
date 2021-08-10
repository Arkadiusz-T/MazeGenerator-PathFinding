class Maze:
    def __init__(self):
        self.structure = list()
        self.size = 0
        self.type = 'Undefined'
        self.entries = list()
        self.solution = list()

    def set_whole_structure(self, new_structure):
        self.structure = new_structure

    def get_whole_structure(self):
        return self.structure

    def destroy_wall(self, coordinates):
        self.structure[coordinates[0], coordinates[1]] = ' '

    def print_maze(self):
        for row in self.structure:
            line = str()
            for j in row:
                line += j
                line += ' '
            print(line)

    def print_solution(self):
        if not self.solution:
            print("No solution was found yet, use PathFinder to get one")
        else:
            for row in self.solution:
                line = str()
                for j in row:
                    line += j
                    line += ' '
                print(line)

