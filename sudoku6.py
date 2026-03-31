from typing import Callable,Tuple, List
import sys
import clingo
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        self.board = board.sudoku
        self.__initial = []

    def initial(self) -> list[clingo.symbol.Symbol]:

        return [ clingo.Tuple_((clingo.Number(x), clingo.Number(y), clingo.Number(self.board[x,y]))) \
                  for x,y in self.board]


class ClingoApp(clingo.application.Application):
    def print_model(self, model: clingo.Model, printer: Callable[[], None]) -> None:
        sudoku_obj = Sudoku.from_model(model)
        print(sudoku_obj)

    def main(self, ctl, files):
        ctl.load("./sudoku.lp")
        ctl.load("./sudoku_py.lp")
        if files: # Unpack each and save contents to dict
            with open(files[0],"r") as f:
                contents = f.read()
                board = Sudoku.from_str(contents)
                print(contents)
        else:
            raise ValueError("No input")
        context = Context(board)
        ctl.ground([("base", [])], context)
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
