from solutions.leetcode_1396_custom_object import (
    UndergroundSystem as CustomObjectSolution,
)
from solutions.leetcode_1396_hash_table import (
    UndergroundSystem as HashTableSolution,
)
from typing import Annotated


class FunctionHelper:
    def __init__(
        self,
        underground_system: Annotated[CustomObjectSolution, HashTableSolution],
    ):
        self.underground_system = underground_system
        self.output = [None]

    def invoke_methods(self, method_names, method_args):
        for method_name, method_arg in zip(method_names, method_args):
            method = getattr(self.underground_system, method_name)
            self.output.append(method(*method_arg))
        return self.output
