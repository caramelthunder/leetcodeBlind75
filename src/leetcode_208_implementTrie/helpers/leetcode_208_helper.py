from solutions.leetcode_208_solution import Trie

class Helper:
    def execute_methods(self, trie: Trie, method_names: list[str], method_args: list[str]) -> list[bool]:
        ans = []
        if trie:
            ans.append(None)

        for i in range(1, len(method_names)):
            try:
                method = getattr(trie, method_names[i])
                ans.append(method(method_args[i][0]))
            except:
                print('Method "{}" not found!'.format(method_names[i]))

        return ans