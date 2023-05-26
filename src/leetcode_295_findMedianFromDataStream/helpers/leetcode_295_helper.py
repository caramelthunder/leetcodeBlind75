class Helper:
    def function_helper(self, solution, method_names, method_args):
        if not solution:
            return []

        output = [None]
        for method_name, method_arg in zip(method_names[1:], method_args[1:]):
            method = getattr(solution, method_name)
            if method_arg:
                output.append(method(*method_arg))
            else:
                output.append(method())

        return output
