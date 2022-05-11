import Solver
import queue as Q
from Board import Board
import math

# In this Implement search algorithms (BFS, DFS, Greedy, A*) to find solution to the sliding puzzle problem:



NeedHueristic = False

class Node:
#Creating Node class from given board state

  def __init__(self, BoardState, StateParent = None):

    self.state = BoardState
    self.goalDist = 0
    self.Heuristic = 0
    self.finalHeu = 0
    self.BoarsizeInt = int(math.sqrt(len(BoardState)))
    self.board = Board(self.BoarsizeInt, BoardState)
    #Checking Condition for Heuristic required or not
    if(NeedHueristic) :
      if StateParent is not None:
        self.goalDist = StateParent.goalDist + 1
      self.Heuristic = self.board.ManhattDistanceForHeuristic(self.board.Goal_State)
      self.finalHeu = self.goalDist + self.Heuristic

    self.parent = StateParent

  def __lt__(self, other):
    return self.finalHeu < other.finalHeu
  
  def __eq__(self, o: object) -> bool:
      return str(self.board) == str(o)
  def __str__(self) -> str:
      return str(self.board)





def AStar_ManhattanD(board):
  
 #AStar implementation

  Solver.NeedHueristic = True

  NumCreated = 0
  NumExpanded = 0
  MaxFringe = 0
  PrintStr = ""

  visited = []
  Not_Visited_Nodes = Q.PriorityQueue()
  Not_Visited_Nodes.put(Node(board.state))

  while not Not_Visited_Nodes.empty():
    NewNodeCur = Not_Visited_Nodes.get();
    NumExpanded += 1
    node_depth = -1
    PathHistory =[]

    if NewNodeCur.board.Goal_State == NewNodeCur.state:
      return GeneratingSolutionForAStar(PathHistory, NewNodeCur, MaxFringe, node_depth, NumCreated, NumExpanded,
                                        PrintStr)
  
    visited.append(NewNodeCur)


    NextStatesFromCurrectState = NewNodeCur.board.generate_NextStatesFromCurrectState()
    NumCreated += len(NextStatesFromCurrectState)
    MaxFringe = max(MaxFringe, Not_Visited_Nodes.qsize())
    for next_state in NextStatesFromCurrectState:
      next_node = Node(next_state, NewNodeCur)
      if next_node not in visited:
        Not_Visited_Nodes.put(next_node)

  return None, PrintStr


def GeneratingSolutionForAStar(PathHistory, NewNodeCur, MaxFringe, DepthOfNode, NumCreated, NumExpanded, PrintStr):
  NewNodeCur_depth = -1
  while NewNodeCur is not None:
    NewNodeCur_depth += 1
    PathHistory.append(str(NewNodeCur.board))
    NewNodeCur = NewNodeCur.parent

  PathHistory.reverse()
  PrintStr += f"Depth : [{NewNodeCur_depth}], Num Created : [{NumCreated}], Num Expanded :[{NumExpanded}], Max Fringe [{MaxFringe}] \n"
  return PathHistory, PrintStr


def GreeedyBestFirstSearch(board):
 # Greedy  best first search approach with heuristics calculated using manhattan distance
 Solver.NeedHueristic = True

 NumCreated = 0
 NumExpanded = 0
 MaxFringe = 0
 PrintStr = ""

 visited = []
 Not_Visited_Nodes = Q.PriorityQueue()
 Not_Visited_Nodes.put(Node(board.state))

 while not Not_Visited_Nodes.empty():
   NewNodeCur = Not_Visited_Nodes.get();
   NumExpanded += 1
   node_depth = 0
   PathHistory = []

   if NewNodeCur.board.Goal_State == NewNodeCur.state:
     return GeneratingSolutionForAStar(PathHistory, NewNodeCur, MaxFringe, node_depth, NumCreated, NumExpanded,
                                       PrintStr)

   visited.append(NewNodeCur)

   NextStatesFromCurrectState = NewNodeCur.board.generate_NextStatesFromCurrectState()
   NumCreated += len(NextStatesFromCurrectState)
   MaxFringe = max(MaxFringe, Not_Visited_Nodes.qsize())
   for next_state in NextStatesFromCurrectState:
     next_node = Node(next_state, NewNodeCur)
     if next_node not in visited:
       Not_Visited_Nodes.put(next_node)

 return None, PrintStr


def GeneratingSolutionForGBFS(PathHistory, NewNodeCur, MaxFringe, DepthOfNode, NumCreated, NumExpanded, PrintStr):
  NewNodeCur_depth = -1
  while NewNodeCur is not None:
    NewNodeCur_depth += 1
    PathHistory.append(str(NewNodeCur.board))
    NewNodeCur = NewNodeCur.parent

  PathHistory.reverse()
  PrintStr += f"Depth : [{NewNodeCur_depth}], Num Created : [{NumCreated}], Num Expanded :[{NumExpanded}], Max Fringe [{MaxFringe}] \n"
  return PathHistory, PrintStr



def BreadthFirstSearch(board):

  Solver.NeedHueristic = False

  NumCreated = 0
  NumExpanded = 0
  MaxFringe = 0
  queue = []
  parentdict = dict();
  visited = set()
  PathStartToGoal = []
  queue.append(Node(board.state, None))
  visited.add(str(board))

  PrintStr = ""



  while len(queue) > 0:
    NumExpanded += 1
    next_state = queue.pop(0)
    parentdict[next_state.board] = next_state.parent;
    if next_state.board.CheckGoalState():
      NewNodeCur_depth = -1
      while next_state is not None:
        NewNodeCur_depth += 1
        PathStartToGoal.append(str(next_state.board))
        next_state = next_state.parent

      PathStartToGoal.reverse()
      PrintStr += f"Depth : [{NewNodeCur_depth}], Num Created : [{NumCreated}], Num Expanded :[{NumExpanded}], Max Fringe [{MaxFringe}] \n"
      return PathStartToGoal, PrintStr

    NextStatesFromCurrectState = next_state.board.generate_NextStatesFromCurrectState()
    NumCreated += len(NextStatesFromCurrectState)
    MaxFringe = max(MaxFringe, len(queue) + len(NextStatesFromCurrectState))
    for state in NextStatesFromCurrectState:
      if "".join(state) not in visited:
        stringified_state = "".join(state)
        board_state = Node(stringified_state, next_state)
        visited.add(stringified_state)
        queue.append(board_state)


  # return the PathStartToGoal of the board
  return PathStartToGoal, PrintStr


def DepthFirstSearch(board, NumCreated = 0, NumExpanded = 0, MaxFringe = 0):
  #This implements DepthFirstSearch
  Solver.NeedHueristic = False
  PrintStr = ""
  stack = []
  visited = set()
  PathStartToGoal = []
  stack.append(Node(board.state, None))
  visited.add(str(board))

  while len(stack) > 0:

    NumExpanded += 1
    next_state = stack.pop()


    if next_state.board.CheckGoalState():
      NewNodeCur_depth = -1
      while next_state is not None:
        NewNodeCur_depth += 1
        PathStartToGoal.append(str(next_state.board))
        next_state = next_state.parent

      PathStartToGoal.reverse()
      PrintStr += f"Depth : [{NewNodeCur_depth}], Num Created : [{NumCreated}], Num Expanded :[{NumExpanded}], Max Fringe [{MaxFringe}] \n"

      return PathStartToGoal, PrintStr

    # Next states from present state
    NextStatesFromCurrectState = next_state.board.generate_NextStatesFromCurrectState()
    NumCreated += len(NextStatesFromCurrectState)
    MaxFringe = max(MaxFringe, len(stack) + len(NextStatesFromCurrectState))

    for state in NextStatesFromCurrectState:

      if "".join(state) not in visited:
        # Add Visited Node
        stringified_state = "".join(state)
        board_state = Node(stringified_state, next_state)
        visited.add(stringified_state)
        stack.append(board_state)



  return PathStartToGoal, PrintStr



