from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given a string s and a string t, return the minimum window in s which will
        contain all the characters in t. If there is no such window in s that covers
        all characters in t, return an empty string "".

        Time complexity: O(|s| + |t|) where |s| and |t| are the lengths of the strings s and t, respectively.
        Space complexity: O(|t|) where |t| is the length of the string t.

        Args:
        s (str): The input string to search for the target characters.
        t (str): The target string containing characters to search for in s.

        Returns:
        str: The minimum window in s containing all characters in t, or an empty string if not found.
        """
        ns = len(s)
        # Count character occurrences in t and initialize an empty counter for s
        td, sd = Counter(t), Counter() 
        # Initialize counters for the number of matched characters and required characters 
        match_count, required_count = 0, len(td)  

        res = (None, None, float('inf'))  # Initialize the result tuple (left, right, window_size)
        left, right = 0, 0  # Initialize left and right pointers

        while right < ns:
            char = s[right]
            if char in td:
                sd[char] += 1  # Increment the character count in the sliding window
                if sd[char] == td[char]:
                    match_count += 1  # Increment the match_count when the character count matches the target

            # Check if the current window contains all characters in t
            while left <= right and match_count == required_count:
                # Update the result if the current window is smaller than the previous minimum window
                if right - left + 1 <= res[2]:
                    res = (left, right, (right - left + 1))

                char = s[left]
                sd[char] -= 1  # Decrement the character count as the window slides
                if char in td and sd[char] < td[char]:
                    match_count -= 1  # Decrement the match_count when the character count is less than the target
                left += 1  # Move the left pointer to the right

            right += 1  # Move the right pointer to the right

        left, right, size = res
        mws = s[left: right + 1] if size != float('inf') else ""
        return mws
