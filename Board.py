
# created Board class (converts string input to n * n board)
#implemented all board related funtionalities


class Board:


  def __init__(self, BoardSize, BoardState) -> None:
    #checking board validitity
    self.checkBoardValidity(BoardSize)

    self.intializeBoard(BoardSize)
    #convert given str char to int
    self.IntializeNumboard()
    self.state = list(BoardState)
    self.GoalStatesOnSize()

  def IntializeNumboard(self):
    self.NumToCharDict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, ' ': 0,
                          }
    self.pathUntilNow = []

  def intializeBoard(self, BoardSize):
    self.size = BoardSize
    self.path_cost = 0
    self.Goal_State = ""

  def checkBoardValidity(self, BoardSize):
    if BoardSize < 2 or BoardSize > 5:
      raise ValueError("Please insert board of size between 2 to 5")


  def __str__(self) -> str:
    #convert to string
    return ''.join(self.state)

  def GoalStatesOnSize(self):

    if self.size == 2:
      self.Goal_State = list("123 ")
      self.NumToCharDict[' '] = 4
    elif self.size == 3:
      self.Goal_State = list(" 12345678")
      self.NumToCharDict[' '] = 0
    elif self.size == 4:
      self.Goal_State = list("123456789ABCDEF ")
      self.NumToCharDict[' '] = 16
    elif self.size == 5:
      self.Goal_State = list("123456789ABCDEFGHIJKLMNO ")
      self.NumToCharDict[' '] = 25



  def get_Next_states(self):

    emptySquare_index = self.state.index(' ')
    emptySquare_row = emptySquare_index // self.size
    emptySquare_col = emptySquare_index % self.size
    Next_states = []

    if emptySquare_row > 0:
      Next_states.append(emptySquare_index - self.size)
    if emptySquare_row < self.size - 1:
      Next_states.append(emptySquare_index + self.size)
    if emptySquare_col > 0:
      Next_states.append(emptySquare_index - 1)
    if emptySquare_col < self.size - 1:
      Next_states.append(emptySquare_index + 1)

    return Next_states
  
  def generate_NextStatesFromCurrectState(self):

    Next_states = self.get_Next_states()
    nextResult = []

    for move in Next_states:
      new_state = self.state.copy()
      temp = new_state[move]
      new_state[move] = new_state[self.state.index(' ')]
      new_state[self.state.index(' ')] = temp
      nextResult.append(new_state)
    
    return nextResult

  def ManhattDistanceForHeuristic(self, result):
    #function to calculate manhattan distance
    rangeBoard = self.size ** 2
    return sum(abs(self.NumToCharDict[result[i]] - self.NumToCharDict[self.state[i]]) for i in range(rangeBoard))

  def HeuristicGenerate(self, outome):
    #funciton to calculate hueristic
    
    emptySquare_index = list(outome).index(' ')
    emptySquare_row = emptySquare_index // self.size
    emptySquare_col = emptySquare_index % self.size
    goal_state_index = list(self.Goal_State).index(' ')
    goal_state_row = goal_state_index // self.size
    goal_state_col = goal_state_index % self.size
    heuristic_value = abs(goal_state_row - emptySquare_row) + abs(goal_state_col - emptySquare_col)

    return heuristic_value
  

  
  def move_emptySquare(self, next_state):

    # update path before going to next state
    self.pathUntilNow.append(self.state)
    self.state = next_state
  
  def CheckGoalState(self):

    if self.size == 2:
      return str(self) == "123 "
    elif self.size == 3:
      return str(self) == " 12345678"
    elif self.size == 4:
      return str(self) == "123456789ABCDEF "
    elif self.size == 5:
      return str(self) == "123456789ABCDEFGHIJKLMNOP "

  def Check_Board_Solvability(self) -> bool:

    BlankRow = 0
    inversions = 0
    #This function checks board solvability
    for i in range(self.size ** 2):
      if self.state[i] == ' ':
        BlankRow = i // self.size
        continue

      for j in range(i + 1, self.size ** 2):
        if self.state[j] == ' ':
          continue
        if self.NumToCharDict[self.state[i]] > self.NumToCharDict[self.state[j]]:
          inversions += 1

    if self.size % 2 == 1:
      return inversions % 2 == 0
    else:
      return (inversions + BlankRow) % 2 == 1
  

  