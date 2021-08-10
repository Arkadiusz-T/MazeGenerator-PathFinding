from Maze import Maze
from random import randint, shuffle, choice


class MazeBuilder:
    @staticmethod
    def create_empty_maze():
        return Maze()

    @staticmethod
    def fill_maze_with_cells(maze, size):
        new_structure = list()
        height = size[0]
        width = size[1]
        wall = list()
        for i in range((width * 2) + 1):
            wall.append('#')

        for row in range(height):
            new_row = list()
            for col in range(width):
                new_row.append('#')
                new_row.append(' ')
            new_row.append('#')
            new_structure.append(wall.copy())
            new_structure.append(new_row)

        new_structure.append(wall)
        maze.set_whole_structure(new_structure)
        maze.size = size
        return maze

    @staticmethod
    def convert_cell_maze_to_perfect_maze(maze, dig_from=[1, 1]):
        size = maze.size
        list_of_visited_cells = list()
        list_of_visited_cells.append(dig_from)
        current_cell = 0
        maze_not_ended = True
        while maze_not_ended:
            dig_from = list_of_visited_cells[current_cell]
            direction = randint(0, 3)
            #direction = 2
            can_dig = False
            if direction == 0:
                # go up
                potential_next_cell = [dig_from[0] - 2, dig_from[1]]
                if potential_next_cell not in list_of_visited_cells and potential_next_cell[0] > 0:
                    can_dig = True
                else:
                    can_dig = False

                if can_dig:
                    maze.structure[dig_from[0] - 1][dig_from[1]] = ' '
                    list_of_visited_cells.append([dig_from[0] - 2, dig_from[1]])
                    current_cell += 1

            elif direction == 1:
                # go right
                potential_next_cell = [dig_from[0], dig_from[1] + 2]
                if potential_next_cell not in list_of_visited_cells and potential_next_cell[1] < size[1]*2:
                    can_dig = True
                else:
                    can_dig = False

                if can_dig:
                    maze.structure[dig_from[0]][dig_from[1] + 1] = ' '
                    list_of_visited_cells.append([dig_from[0], dig_from[1] + 2])
                    current_cell += 1

            elif direction == 2:
                # go down
                potential_next_cell = [dig_from[0] + 2, dig_from[1]]
                if potential_next_cell not in list_of_visited_cells and potential_next_cell[0] < size[1] * 2:
                    can_dig = True
                else:
                    can_dig = False

                if can_dig:
                    maze.structure[dig_from[0] + 1][dig_from[1]] = ' '
                    list_of_visited_cells.append([dig_from[0] + 2, dig_from[1]])
                    current_cell += 1

            elif direction == 3:
                # go left
                potential_next_cell = [dig_from[0], dig_from[1] - 2]
                if potential_next_cell not in list_of_visited_cells and potential_next_cell[1] > 0:
                    can_dig = True
                else:
                    can_dig = False

                if can_dig:
                    maze.structure[dig_from[0]][dig_from[1] - 1] = ' '
                    list_of_visited_cells.append([dig_from[0], dig_from[1] - 2])
                    current_cell += 1

            if not can_dig:
                # go round list of visited spots until all visited
                if size[0] * size[1] == len(list_of_visited_cells):
                    maze_not_ended = False

                current_cell = (current_cell - 1) % len(list_of_visited_cells)
        return maze

    @staticmethod
    def convert_perfect_maze_to_non_perfect(maze):
        return maze

    @staticmethod
    def add_distance_to_maze(maze):
        size = maze.size
        for row in range(size[0]*2+1):
            for col in range(size[1]*2+1):
                cell = maze.structure[row][col]
                if cell == ' ':
                    maze.structure[row][col] = str(randint(1, 9))
        return maze

    @staticmethod
    def create_entries_to_maze(maze, n_of_entries=2):
        size = maze.size
        while len(maze.entries) != n_of_entries:
            chose_entry_wall = randint(0, 3)
            potential_entry = list()
            if chose_entry_wall == 0:
                # upper wall
                potential_entry = [0, randint(1, size[1] * 2 - 1)]
                if maze.structure[potential_entry[0] + 1][potential_entry[1]] == '#'\
                   or maze.structure[potential_entry[0]][potential_entry[1] + 1] != '#'\
                   or maze.structure[potential_entry[0]][potential_entry[1] - 1] != '#':
                    # there is no wall after entry
                    # and no entry beside new entry
                    potential_entry = 'not valid'

            if chose_entry_wall == 1:
                # right wall
                potential_entry = [randint(1, size[0] * 2 - 1), size[1] * 2]
                if maze.structure[potential_entry[0]][potential_entry[1] - 1] == '#'\
                   or maze.structure[potential_entry[0] - 1][potential_entry[1]] != '#'\
                   or maze.structure[potential_entry[0] + 1][potential_entry[1]] != '#':
                    # there is no wall after entry
                    # and no entry beside new entry
                    potential_entry = 'not valid'

            if chose_entry_wall == 2:
                # lower wall
                potential_entry = [size[0] * 2, randint(1, size[1] * 2 - 1)]
                if maze.structure[potential_entry[0] - 1][potential_entry[1]] == '#'\
                   or maze.structure[potential_entry[0]][potential_entry[1] + 1] != '#'\
                   or maze.structure[potential_entry[0]][potential_entry[1] - 1] != '#':
                    # there is no wall after entry
                    # and no entry beside new entry
                    potential_entry = 'not valid'

            if chose_entry_wall == 3:
                potential_entry = [randint(1, size[1] * 2 - 1), 0]
                if maze.structure[potential_entry[0]][potential_entry[1] + 1] == '#'\
                   or maze.structure[potential_entry[0] - 1][potential_entry[1]] != '#'\
                   or maze.structure[potential_entry[0] - 1][potential_entry[1]] != '#':
                    # there is no wall after entry
                    # and no entry beside new entry
                    potential_entry = 'not valid'

            if potential_entry not in maze.entries and potential_entry != 'not valid':
                # we did not choose existing entry, not beside old one, not in front of the wall
                maze.structure[potential_entry[0]][potential_entry[1]] = ' '
                maze.entries.append(potential_entry)

        return maze
