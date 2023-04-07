class Solution:
    """
    Given an integer n, return the next greater permutation of its digits. If it does not exist, return -1.
    
    Args:
    - n: An integer
    
    Returns:
    - The next greater permutation of n
    
    Example:
    Input: n = 1234
    Output: 1243

    Convert the list of digits to an integer and check if it is within the valid range
    # Time complexity: O(n), where n is the number of digits in n.
    # Space complexity: O(n), as we create a list of digits to store the digits in n.
    """

    def nextGreaterElement(self, n: int) -> int:
        # Convert n to a list of digits
        nums = list(str(n))

        # Find the pivot index, where the digit at the pivot index is smaller than the digit to its right
        pivot = len(nums) - 2
        while pivot >=0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        
        # If pivot is not found, the digits are in descending order, so the next greater permutation does not exist
        if pivot < 0: return -1

        # Find the smallest digit to the right of the pivot that is greater than the pivot digit
        i = len(nums) - 1
        while i > pivot and nums[pivot] >= nums[i]:
            i -= 1
        
        # Swap the pivot digit with the next greater digit to its right
        nums[pivot], nums[i] = nums[i], nums[pivot]

        # Reverse the digits to the right of the pivot
        res = nums[: pivot + 1] + nums[-1: pivot: -1]
        
        res = int(''.join(res))
        return res if n < res <= 2**31 - 1 else -1
