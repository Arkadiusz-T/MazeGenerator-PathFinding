from random import randint


class PathFinder:
    @staticmethod
    def random_mouse_algorithm(maze, size=[10, 10]):
        solution = maze.structure
        current_location = maze.entries[0]
        solution_not_ended = True
        end_location = maze.entries[1]
        direction = int()
        can_make_a_step = True

        # find first direction to go into the maze
        if maze.entries[0][0] == 0:
            direction = 2

        elif maze.entries[0][1] == 0:
            direction = 1

        elif maze.entries[0][0] == size[0] * 2:
            direction = 0

        elif maze.entries[0][1] == size[1] * 2:
            direction = 3

        while solution_not_ended:
            while can_make_a_step:
                potential_next_location = list()
                try:
                    potential_next_locations = list()
                    potential_next_locations.append(solution[current_location[0] - 1][current_location[1]])
                    potential_next_locations.append(solution[current_location[0]][current_location[1] + 1])
                    potential_next_locations.append(solution[current_location[0] + 1][current_location[1]])
                    potential_next_locations.append(solution[current_location[0]][current_location[1] - 1])
                    if potential_next_locations.count('#') != 2:
                        # if on junction try to change direction
                        direction = randint(0, 3)
                except IndexError:
                    #  near end of the maze
                    pass
                if direction == 0:
                    # go up
                    potential_next_location = [current_location[0] - 1, current_location[1]]

                elif direction == 1:
                    # go right
                    potential_next_location = [current_location[0], current_location[1] + 1]

                elif direction == 2:
                    # go down
                    potential_next_location = [current_location[0] + 1, current_location[1]]

                elif direction == 3:
                    # go left
                    potential_next_location = [current_location[0], current_location[1] - 1]

                try:
                    if potential_next_location != maze.entries[0]:
                        if solution[potential_next_location[0]][potential_next_location[1]] != '#':
                            solution[current_location[0]][current_location[1]] = '.'
                            current_location = potential_next_location

                except IndexError:
                    solution[current_location[0]][current_location[1]] = '.'
                    maze.solution = solution
                    can_make_a_step = False
                    solution_not_ended = False
                    print(current_location, potential_next_location)

                else:
                    can_make_a_step = False

                if not current_location != end_location:
                    can_make_a_step = False
                    solution_not_ended = False
                maze.solution = solution
            direction = randint(0, 3)
            can_make_a_step = True
        solution[maze.entries[1][0]][maze.entries[1][1]] = '.'
        maze.solution = solution

    @staticmethod
    def wall_follower(self):
        pass

    @staticmethod
    def tremaux_algorithm():
        pass

