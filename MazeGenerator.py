from MazeBuilder import MazeBuilder


class MazeGenerator:
    @staticmethod
    def create_perfect_maze(size=[10, 10]):
        maze = MazeBuilder.create_empty_maze()
        maze = MazeBuilder.fill_maze_with_cells(maze, size)
        maze = MazeBuilder.convert_cell_maze_to_perfect_maze(maze)
        maze = MazeBuilder.create_entries_to_maze(maze)
        return maze

    @staticmethod
    def create_non_perfect_maze(size=[10, 10]):
        maze = MazeBuilder.create_empty_maze()
        maze = MazeBuilder.fill_maze_with_cells(maze, size)
        maze = MazeBuilder.convert_cell_maze_to_perfect_maze(maze, size)
        maze = MazeBuilder.convert_perfect_maze_to_non_perfect(maze, size)
        return maze

    @staticmethod
    def create_non_perfect_maze_with_distances(size=[10, 10]):
        maze = MazeBuilder.create_empty_maze()
        maze = MazeBuilder.fill_maze_with_cells(maze, size)
        maze = MazeBuilder.convert_cell_maze_to_perfect_maze(maze, size)
        maze = MazeBuilder.convert_perfect_maze_to_non_perfect(maze, size)
        maze = MazeBuilder.add_distance_to_maze(maze, size)
        return maze
