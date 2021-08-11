from random import randint


class PathFinder:
    @staticmethod
    def random_mouse_algorithm(maze):
        # declare variables
        size = maze.size
        solution = maze.structure           # placeholder for solution
        current_location = maze.entries[0]  # start search from the entry
        solution_not_ended = True           # solution it yet to find
        end_location = maze.entries[1]      # set exit coordinates
        direction = int()
        can_make_a_step = True              # there is no wall in front of the entry

        # find first direction to go into the maze
        if current_location[0] == 0:
            direction = 2

        elif current_location[1] == 0:
            direction = 1

        elif current_location[0] == size[0] * 2:
            direction = 0

        elif current_location[1] == size[1] * 2:
            direction = 3

        while solution_not_ended:
            # continue until algorithm reach the exit
            while can_make_a_step:
                #
                potential_next_location = list()
                try:
                    # check if on junction
                    potential_next_locations = list()
                    potential_next_locations.append(solution[current_location[0] - 1][current_location[1]])
                    potential_next_locations.append(solution[current_location[0]][current_location[1] + 1])
                    potential_next_locations.append(solution[current_location[0] + 1][current_location[1]])
                    potential_next_locations.append(solution[current_location[0]][current_location[1] - 1])
                    if potential_next_locations.count('#') != 2:
                        # if on junction then try to change direction
                        direction = randint(0, 3)
                except IndexError:
                    # first or last iteration of the algorithm, there is no wall to prevent it from moving
                    # there is no need to check fot a junction
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

                if potential_next_location != maze.entries[0] \
                   and solution[potential_next_location[0]][potential_next_location[1]] != '#':
                    solution[current_location[0]][current_location[1]] = '.'
                    current_location = potential_next_location
                else:
                    can_make_a_step = False

                if current_location == end_location:
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

