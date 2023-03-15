class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        trie = TrieNode()
        trie.add_word(word)

        R, C = len(board), len(board[0])

        def _dfs(row, col, trie_node):
            if row < 0 or row >= R or col < 0 or col >= C or board[row][col] not in trie_node.children:
                return False

            ch, board[row][col] = board[row][col], "#"
            next_node = trie_node.children[ch]

            if next_node.is_word:
                return True

            for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if _dfs(row + _r, col + _c, next_node):
                    return True

            board[row][col] = ch
            return False

        for row in range(R):
            for col in range(C):
                if _dfs(row, col, trie):
                    return True

        return False
