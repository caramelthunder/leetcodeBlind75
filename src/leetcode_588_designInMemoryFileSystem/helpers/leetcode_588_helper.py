from typing import Union

from solutions.leetcode_588_solution import FileSystem as FileSystem
from solutions.leetcode_588_with_simple_cache import (
    FileSystem as SimpleCacheFileSystem,
)
from solutions.leetcode_588_with_complex_cache import (
    FileSystem as ComplexCacheFileSystem,
)


class FunctionHelper:
    def __init__(
        self,
        file_system: Union[
            FileSystem, SimpleCacheFileSystem, ComplexCacheFileSystem
        ],
    ):
        self.file_system = file_system
        self.output = [None]

    def execute_methods(self, names, inputs):
        for name, input in zip(names[1:], inputs[1:]):
            try:
                method = getattr(self.file_system, name)
                self.output.append(method(*input))
            except Exception as e:
                print(
                    f"Exception occurred while executing {name}({input}): {e}"
                )
        return self.output
