from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
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
