from typing import Callable,Tuple, List
import sys
import clingo
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        self.__initial = board.sudoku

    def initial(self) -> list[clingo.symbol.Symbol]:

        stuff = [ clingo.Tuple_((clingo.Number(x[0]), clingo.Number(x[1]), clingo.Number(v))) \
                 for x,v in self.__initial.items() ]
        return stuff

        # YOUR CODE HERE

class ClingoApp(clingo.application.Application):
    def print_model(self, model: clingo.Model, printer: Callable[[], None]) -> None:
        sudoku_obj = Sudoku.from_model(model)
        print(sudoku_obj)

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.load("./sudoku.lp")
        ctl.ground()
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
