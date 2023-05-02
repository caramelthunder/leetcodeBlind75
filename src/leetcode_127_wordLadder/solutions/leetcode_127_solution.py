from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        Calculates the length of the shortest transformation sequence 
        from `beginWord` to `endWord` using the words from `wordList`.

        :param str beginWord: The starting word of the transformation sequence.
        :param str endWord: The target word of the transformation sequence.
        :param list[str] wordList: A list of available words to use for the transformation.
        :return int: The length of the shortest transformation sequence, or 0 if no such sequence exists.

        Time Complexity: O(n * k^2), where n is the number of words in `wordList` and k is the maximum length of a word.
        Space Complexity: O(n * k^2), for the graph and the visited set.
        """

        if (beginWord == "") or (endWord == "") or (endWord not in wordList) or (not wordList): 
            return 0

        graph = self._build_graph(wordList)
        visited = set()

        q = deque([(beginWord, 1)])
        visited.add(beginWord)

        while q:
            curr_word, cnt = q.popleft()
            
            for wildcard in self._get_wildcards(curr_word):
                for word in graph.get(wildcard, []):

                    # Catch result early.
                    if word == endWord:
                        return cnt + 1

                    if word not in visited:
                        visited.add(word)
                        q.append((word, cnt + 1))

        return 0
    
    def _get_wildcards(self, word):
        """
        Generates a list of wildcard representations of the given word.

        :param str word: The input word.
        :return list[str]: A list of wildcard representations of the input word.
        """
        return [word[:i] + "*" + word[i + 1:] for i in range(len(word))]
    
    def _build_graph(self, wordList):
        """
        Builds a graph representation of the given word list using wildcard representations.

        :param list[str] wordList: A list of words.
        :return: A dictionary representing the graph, where the keys are wildcard representations 
        and the values are lists of words that match the wildcard.
        """
        graph = {}
        for word in wordList:
            for wildcard in self._get_wildcards(word):
                if wildcard not in graph:
                    graph[wildcard] = []
                graph[wildcard].append(word)
        return graph
