class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Args:
        - nums1: A list of integers representing the first array
        - nums2: A list of integers representing the second array
        
        Returns:
        - A list of integers representing the next greater element for each element in nums1
        
        Example:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        Output: [-1,3,-1]

        '''
        Time complexity: O(m+n), where m is the length of nums1 and n is the length of nums2.

        Space complexity: O(m+n), as we use a map to store the next greater element for each element in nums2,
        which takes O(n) space, and we create a list to store the next greater element for each element in nums1,
        which takes O(m) space. 
        
        Therefore, the overall space complexity is O(m+n).
        '''
        """
        
        # Create a map to store the next greater element for each element in nums2
        num_nge_map = {}
        
        # Create a monotonic stack to keep track of elements in nums2
        monotonic_stack = []

        # Iterate through each element in nums2
        for num in nums2:
            
            # While the stack is not empty and the top element is less than the current element
            while monotonic_stack and monotonic_stack[-1] < num:
                
                # Pop the top element from the stack and set its next greater element to the current element
                num_nge_map[monotonic_stack[-1]] = num
                monotonic_stack.pop()

            # Add the current element to the stack
            monotonic_stack.append(num)

        return [num_nge_map.get(num, -1) for num in nums1]
