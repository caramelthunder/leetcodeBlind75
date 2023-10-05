from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """
        Returns all strobogrammatic numbers that are of length n.
        
        A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
        
        Parameters:
        - n (int): The length of numbers to be returned.
        
        Returns:
        - List[str]: A list of strobogrammatic numbers of length n.
        
        Time Complexity:
        - The time complexity is O(5^(n/2)) because at each recursive step, we have 5 choices 
          (4 strobogrammatic pairs and 1 for '0'). The depth of the recursion is n/2.
          
        Space Complexity:
        - The space complexity is O(n) due to the recursive call stack.
        """
        
        def _findStrobogrammatic(_n: int):
            # Base cases
            if _n == 0:
                return ['']
            if _n == 1:
                return ['0', '1', '8']
            
            # Recursively get the centers for the current _n
            centers = _findStrobogrammatic(_n - 2)

            # Construct the strobogrammatic numbers using the centers
            # and the possible strobogrammatic pairs
            output = []
            for center in centers:
                for start, end in [('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]:
                    output.append(start + center + end)
                # Add '0' only if it's not the outermost layer to avoid leading zeros
                if _n != n:
                    output.append('0' + center + '0')
            return output
        
        return _findStrobogrammatic(n)