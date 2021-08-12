from MazeGenerator import MazeGenerator
from PathFinder import PathFinder
from time import sleep

# right now only square mazes are supported
size = [10, 10]

print("This is perfect maze solved by random mouse algorithm:")
sleep(1)
maze = MazeGenerator.create_perfect_maze(size=size)
PathFinder.random_mouse_algorithm(maze)
maze.print_solution()
sleep(1)
print('--------------------------------------------')
sleep(1)
print("This is perfect maze solved by wall follower algorithm:")
sleep(1)
maze2 = MazeGenerator.create_perfect_maze(size=size)
PathFinder.wall_follower(maze2)
maze2.print_solution()
sleep(1)
print('--------------------------------------------')
sleep(1)
print("This is non-perfect maze solved by random mouse algorithm:")
sleep(1)
maze3 = MazeGenerator.create_non_perfect_maze(size=size)
PathFinder.random_mouse_algorithm(maze3)
maze3.print_solution()
sleep(1)
print('--------------------------------------------')
sleep(1)
print("This is non-perfect maze solved by wall follower algorithm:")
sleep(1)
maze4 = MazeGenerator.create_non_perfect_maze(size=size)
PathFinder.wall_follower(maze4)
maze4.print_solution()
sleep(1)
