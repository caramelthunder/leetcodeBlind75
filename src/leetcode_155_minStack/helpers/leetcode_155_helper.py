from solutions.leetcode_155_two_stacks import MinStack
from solutions.leetcode_155_one_stack_tuple import MinStack
from solutions.leetcode_155_two_stacks_optimized import MinStack

class Helper:
    def run_methods(self, minStack: MinStack, method_names: list[str], method_args: list[int]) -> list[int]:
        if not minStack:
            return []

        output = [None]
        for method_name, method_arg in zip(method_names[1:], method_args[1:]):
            method = getattr(minStack, method_name)
            output.append(method(method_arg[0]) if method_arg else method())

        return output