import sudokuSolver as ss

solver = ss.SudokuSolver(9)

solver.createPuzzle(0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,9,4,0,0,0,3,0,0,0,0,0,5,0,9,2,3,0,5,0,7,4,8,4,0,0,0,0,0,0,0,0,6,7,0,9,8,0,0,0,0,0,0,7,0,6,0,0,0,0,0,0,9,0,0,0,2,0,4,0,8,5,0,0,3,6,0)

solver.printGrid()
solver.solvePuzzle()
solver.printGrid()

