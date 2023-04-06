class Solution:
    def alienOrder(self, words: list[str]) -> str:
        unique_chars = self._get_unique_chars(words)

        graph, out_degrees = self._build_graph(unique_chars, words)
        if not graph:
            return ""
        
        visiting = set()
        visited = set()
        res = []
        smallest_chars = [char for char in unique_chars if out_degrees[char] == 0]

        for char in smallest_chars:
            self._alienOrder(graph, res, visiting, visited, char)

        return "".join(res) if len(res) == len(unique_chars) else ""
    
    def _alienOrder(self, graph, res, visiting, visited, char):

        if char in visited:     return True
        if char in visiting:    return False
        
        visiting.add(char)
        for pre_char in graph[char]:
            if not self._alienOrder(graph, res, visiting, visited, pre_char):
                return False
        visiting.remove(char)
        
        visited.add(char)
        res.append(char)
        return True

    def _get_unique_chars(self, words):
        unique_chars = set()
        for word in words:
            for char in word:
                unique_chars.add(char)
        return unique_chars

    def _build_graph(self, unique_chars, words):
        graph = {char: set() for char in unique_chars}
        out_degrees = {char: 0 for char in unique_chars}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            if word1.startswith(word2) and len(word1) > len(word2):
                return ({}, {})
                
            for char_1, char_2 in zip(word1, word2):
                if char_1 != char_2:
                    if char_1 not in graph[char_2]:
                        graph[char_2].add(char_1)
                        out_degrees[char_1] += 1
                    break

        return (graph, out_degrees)