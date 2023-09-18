from typing import List


class Solution:
    """
    This class contains a method to find a missing number in an arithmetic progression.
    
    Time Complexity:
        The time complexity of the missingNumber method is O(log n) because it uses a binary search approach,
        which halves the search space in each iteration.
    
    Space Complexity:
        The space complexity of the method is O(1) as it only uses a constant amount of extra space.
    """
    
    def missingNumber(self, arr: List[int]) -> int:
        """
        This method finds and returns the missing number in the arithmetic progression represented by the input array.
        
        Parameters:
        arr (List[int]): A list of integers where one integer from an arithmetic progression is missing.
        
        Returns:
        int: The missing number in the arithmetic progression.
        """
        
        # Calculate the expected common difference in the arithmetic progression
        expected_diff = (arr[-1] - arr[0]) // len(arr)
        
        # Initialize left and right pointers for binary search
        left, right = 0, len(arr) - 1

        # Perform binary search to find the missing number
        while left < right:
            mid = left + (right - left) // 2

            # If the expected number at the mid position matches the actual number,
            # the missing number is in the right half of the array
            if arr[0] +  mid * expected_diff == arr[mid]:
                left = mid + 1
            # Otherwise, the missing number is in the left half of the array
            else:
                right = mid

        # Calculate and return the missing number
        return arr[0] + left * expected_diff

        