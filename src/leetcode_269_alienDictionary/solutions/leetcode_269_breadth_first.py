from collections import deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        unique_chars = self._get_unique_chars(words)

        graph, in_degrees = self._build_graph(unique_chars, words)
        if not graph:
            return ""
        
        res = ""
        q = deque([char for char in unique_chars if in_degrees[char] == 0])

        while q:
            char = q.popleft()
            res += char

            for next_char in graph[char]:
                in_degrees[next_char] -= 1
                if in_degrees[next_char] == 0:
                    q.append(next_char)

        return res if len(res) == len(unique_chars) else ""

    def _get_unique_chars(self, words):
        unique_chars = set()
        for word in words:
            for char in word:
                unique_chars.add(char)
        return unique_chars

    def _build_graph(self, unique_chars, words):
        graph = {char: set() for char in unique_chars}
        in_degrees = {char: 0 for char in unique_chars}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            if word1.startswith(word2) and len(word1) > len(word2):
                return ({}, {})
                
            for char_1, char_2 in zip(word1, word2):
                if char_1 != char_2:
                    if char_2 not in graph[char_1]:
                        graph[char_1].add(char_2)
                        in_degrees[char_2] += 1
                    break

        return (graph, in_degrees)