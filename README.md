The program “animate_sudoku” solves Sudoku problems and shows the process of solving the puzzles. 

Input the problems in this form:
6 0 0 0 1 0 0 3 7
3 8 0 0 0 7 0 0 9
0 0 9 0 2 4 0 0 0
0 0 8 0 5 0 0 0 0
0 6 0 2 0 0 1 5 0
5 0 0 9 8 6 0 7 4
0 5 0 0 0 8 7 0 3
7 1 0 0 3 2 8 0 0
0 0 0 0 0 5 6 2 1
where the zeros mean blanks to be filled.

The program solves Sudoku problems by Depth First Search; therefore, if a problem has more than one solution, the program provides the answer that if first found. 

“sudoku_generator” randomly generates problems at the level requested and  “sudoku_generator_ed2” further traverses over all solutions to check how many solutions there are.