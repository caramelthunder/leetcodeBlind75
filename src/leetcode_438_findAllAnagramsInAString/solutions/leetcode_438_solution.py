from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # Initialize the char frequency dictionary and string length.
        p_freq, p_len = Counter(p), len(p)
        s_freq, s_len = {char: 0 for char in p}, len(s)
        
        # Initialize the result list, left and right indices of the window
        res = []
        L = R = 0

        for R in range(len(s)):
            # Update the window frequency dictionary
            if s[R] in p_freq:
                s_freq[s[R]] = s_freq.get(s[R], 0) + 1

            # Check if the current window contains an anagram of the pattern
            if s_freq == p_freq:
                res.append(L)
            
            # Shrink the window if its size exceeds the pattern length
            if R - L + 1 >= p_len:
                # Remove the leftmost character from the window
                if s[L] in s_freq:
                    s_freq[s[L]] -= 1
                    if s_freq[s[L]] == 0:
                        del s_freq[s[L]]
                        
                # Move the left pointer to the right until a character in the pattern is found
                L += 1
                while L < s_len and s[L] not in p_freq:
                    L += 1

        return res
