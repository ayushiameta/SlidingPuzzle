from Solver import (
  BreadthFirstSearch,
  DepthFirstSearch,
  AStar_ManhattanD,
  GreeedyBestFirstSearch
)
import sys
import time
from Board import Board


if __name__ == "__main__":

  # get the arguments from the command line in the order:
  # size, StartState, search Method
  # size should be from 2 to 5
  # Example : python3 Tester.py 3 '21345687 ' BFS

  time1 = time.time()
  depth = -1
  NumExpanded = 0
  NumCreated = 0
  MaxFringe = 0
  PrintStr = ""
  board_path = ""

  try:
    #Running with defult arguments
    if( len(sys.argv) == 1 ):
      SearchMethod = "DFS"
      grid_size = 2
      StartState = "23 1"

    else:
      #intializing using given Arguments
      grid_size = int(sys.argv[1])
      StartState = sys.argv[2]
      SearchMethod = sys.argv[3]

  except:
    print("Arguments Not Valid")
    print("Run the program with these Arguments: size, Initial State, Search Algorithm")
    sys.exit(1)

  board = Board(grid_size, StartState)

  # checking whether board is solvable or not
  if not board.Check_Board_Solvability():
    print("Board not solvable")
    sys.exit(1)



  str1 = ''.join(board.state)
  str2 = ''.join(board.Goal_State)
  str3 = "\n**** Search Method : " + SearchMethod + " ****\n"

  fstr = str3 + "\n Size:" + str(grid_size)  + "  Initial State: '" + str1 + "' ==> Goal State: '" + str2 + "'"

  if SearchMethod == "GBFS":
    board_path, PrintStr = GreeedyBestFirstSearch(board)
  elif SearchMethod == "DFS":
    board_path, PrintStr = DepthFirstSearch(board)
  elif SearchMethod == "AStar":
    board_path, PrintStr = AStar_ManhattanD(board)
  elif SearchMethod == "BFS":
    board_path, PrintStr = BreadthFirstSearch(board)


  print("Time taken to run " + SearchMethod)
  time2 = time.time()
  print(time2 - time1)

  # generating readme.txt file

  with open("Readme.txt", "w") as readmeFile:
    readmeFile.write("\n Execution starts with Tester.py with Arguments: size, Initial State, Search Algorithm\n ")
    readmeFile.write(" Example : python3 Tester.py 3 '21345687 ' BFS \n\n ")
    readmeFile.write(fstr)
    readmeFile.write(PrintStr)
    readmeFile.write("\n Path from Start to Goal State \n ")
    readmeFile.write(str(board_path))

  print(fstr)
  print("\n Path from Start state to Goal state : ")
  print(board_path)
  print("")
  print(PrintStr)

