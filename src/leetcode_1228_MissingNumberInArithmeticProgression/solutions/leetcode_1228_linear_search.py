from typing import List


class Solution:
    """
    This class contains a method to find a missing number in an arithmetic progression.
    
    Time Complexity:
        The time complexity of the missingNumber method is O(n), where n is the length of the input array. 
        This is because, in the worst case, the method iterates through the entire array once.
    
    Space Complexity:
        The space complexity of the method is O(1), as it only uses a constant amount of extra space.
    """
    
    def missingNumber(self, arr: List[int]) -> int:
        """
        This method finds and returns the missing number in the arithmetic progression represented by the input array.
        
        Parameters:
        arr (List[int]): A list of integers where one integer from an arithmetic progression is missing.
        
        Returns:
        int: The missing number in the arithmetic progression.
        """
        
        # Get the length of the array
        n = len(arr)
        
        # Calculate the differences between the first two elements and the last two elements
        diff_1 = arr[1] - arr[0]
        diff_2 = arr[-1] - arr[-2]
        
        # Determine the expected difference by comparing the absolute values of diff_1 and diff_2
        expected_diff = diff_1 if abs(diff_1) < abs(diff_2) else diff_2
        
        # Initialize a counter to traverse the array
        i = 0
        
        # Traverse the array until finding a pair of adjacent elements with a difference not equal to the expected difference
        while i < n - 1 and abs(arr[i + 1] - arr[i]) == abs(expected_diff):
            i += 1

        # Calculate and return the missing number
        return arr[i] + expected_diff
