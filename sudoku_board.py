from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        keylist = sorted(list(self.sudoku.keys()))
        # This is hideous

        for key in keylist:
            if ( key[1] == 9 ): # End of table
                s = s + f"{self.sudoku.get(key)}"
                if key[0]%3 == 0: # Pop in an extra newline for vertical subgrid
                    s = s + "\n"
                s = s + "\n"
            elif ( key[1]%3 == 0 ) and (key[1] != 9): # horizontal subgrid
                s = s + f"{self.sudoku.get(key)} "
                s = s + " "
            else: # Normal num
                s = s + f"{self.sudoku.get(key)} "

        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        input = model.symbols(shown=True)
        for symbol in input:
            # Convert symbols (Number(#)) to strings, then to ints, then store
            sudoku[int( str(symbol.arguments[0]) ),int( str(symbol.arguments[1] ))] =\
            int( str(symbol.arguments[2] ))
        return cls(sudoku)
