from solutions.leetcode_981_solution import TimeMap

class Helper:
    def execute_methods(self, instance: TimeMap, method_names: list[str], method_args: list[any]):
        if not instance:
            return []
        
        output = [None]
        for method_name, method_arg in zip(method_names[1:], method_args[1:]):
            method = getattr(instance, method_name)
            output.append(method(*method_arg) if method_arg else method())
        
        return output