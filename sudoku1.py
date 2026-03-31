from typing import Callable, Tuple
import sys
import clingo


class ClingoApp(clingo.application.Application):
    def print_model(self, model: clingo.Model, printer: Callable[[], None]) -> None:
        solution = model.symbols(shown=True)
        solution = [ str(s) for s in solution ]
        solution.sort()
        sys.stdout.write('{}\n'.format(' '.join(solution)))
        sys.stdout.flush()

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
