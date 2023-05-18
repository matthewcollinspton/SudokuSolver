import matplotlib.pyplot as plt

class SudokuSolver:

  def __init__(self, gridSize):
    self.grid = None
    self.gridSize = gridSize
    self.pointsVisited = []


  def createPuzzle(self, *args):
    print("Creating puzzle...")
    print()
    self.grid = [[0]*self.gridSize for i in range(self.gridSize)]

    if len(args) != self.gridSize * self.gridSize:
      print(f"Could not create puzzle. Invalid number of arguments. Expected: {self.gridSize * self.gridSize}. Received: {len(args)}")
      return

    row = 0
    col = 0

    for entry in args:
      self.grid[row][col] = entry

      if (col+1) % self.gridSize == 0:
        col = 0
        row += 1
      else:
        col += 1


  def printGrid(self):

    if self.grid is None:
      print("No grid to print. Try creating a grid first.")
      return
      
    for row in self.grid:
      print(row)
    print()

  def __getColumn(self, col):

    if col >= self.gridSize or col < 0:
      print("Invalid column argument.")
      return None
      
    return [x[col] for x in self.grid]

  def __getRow(self, row):

    if row >= self.gridSize or row < 0:
      print("Invalid row argument.")
      return None

    return self.grid[row]

  def __getGrid(self, row, col):
    colDepth = col // 3
    rowDepth = row // 3

    subGrid = [x[colDepth*3:colDepth*3+3] for x in self.grid[rowDepth*3:rowDepth*3+3]]
    return subGrid    
    
  
  def __isNumberValid(self, row, col, number):

    checkColumn = self.__getColumn(col)
    checkRow = self.__getRow(row)
    subGrid = self.__getGrid(row, col)
    
    if checkRow == None or checkColumn == None:
      return

    for row in subGrid:
      if number in row:
        return False

    if number in checkRow or number in checkColumn:
      return False

    else:
      return True

  def __updateRowAndCol(self, row, col):
    if (col+1) % self.gridSize == 0:
      return row+1, 0
    else:
      return row, col+1

  def __solvePuzzleFromPoint(self, row, col):

    self.pointsVisited.append((row*row)+(col*col))

    if self.grid[row][col] != 0:
      newRow, newCol = self.__updateRowAndCol(row, col)
      return self.__solvePuzzleFromPoint(newRow, newCol)

    else:
      for i in range(self.gridSize+1):
        if self.__isNumberValid(row, col, i):

          self.grid[row][col] = i

          # Adjust row and column
          if (row + 1) == self.gridSize and (col + 1) == self.gridSize:
            return True

          else:
            newRow, newCol = self.__updateRowAndCol(row, col)
            if self.__solvePuzzleFromPoint(newRow, newCol):
              return True
            else:
              self.grid[row][col] = 0
  
      return False


  def solvePuzzle(self):
    row = 0
    col = 0

    return self.__solvePuzzleFromPoint(row, col)


  def plotPoints(self):
    plt.plot(self.pointsVisited)
    plt.show()