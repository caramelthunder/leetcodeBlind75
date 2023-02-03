from solutions.leetcode_232_solution import MyQueue

class Helper:
    def run_methods(self, method_names: list[str], params: list[any]) -> list[any]:
        q = MyQueue()
        output = [None]
        for i in range(1, len(method_names)):
            method = getattr(q, method_names[i])
            output.append(method(*params[i]))
        return output