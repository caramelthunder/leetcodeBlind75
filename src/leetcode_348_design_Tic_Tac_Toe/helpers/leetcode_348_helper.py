from solutions.leetcode_348_solution import TicTacToe


class FunctionHelper:
    def __init__(self, instance: TicTacToe):
        self.instance = instance
        self.output = [None]

    def execute_methods(self, names: list[str], args: list[list[int]]):
        for name, arg in zip(names, args):
            method = getattr(self.instance, name)
            self.output.append(method(*arg))
        return self.output
