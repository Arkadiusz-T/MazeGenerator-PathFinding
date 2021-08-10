from MazeGenerator import MazeGenerator
from PathFinder import PathFinder


maze = MazeGenerator.create_perfect_maze(size=[6, 6])
maze.print_maze()

print('--------------------------------------------')

PathFinder.random_mouse_algorithm(maze)
maze.print_solution()
