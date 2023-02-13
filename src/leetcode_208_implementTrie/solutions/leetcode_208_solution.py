class TrieNode:
    def __init__(self, letter= ''):
        self.letter = letter
        self.next_letters = {}
        self.is_last_letter = False

class Trie(TrieNode):

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.next_letters:
                curr.next_letters[letter] = TrieNode(letter)
            curr = curr.next_letters[letter]
        curr.is_last_letter = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.next_letters:
                return False
            curr = curr.next_letters[letter]
        return curr.is_last_letter

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.next_letters:
                return False
            curr = curr.next_letters[letter]
        return True
