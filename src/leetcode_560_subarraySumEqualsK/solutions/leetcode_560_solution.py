class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculate the total number of continuous subarrays whose sum equals k.

        :param nums: List of integers representing the input array.
        :param k: Integer value to find the sum of subarrays.
        :return: Integer representing the total number of continuous subarrays
                 whose sum equals k.

        Time complexity: O(n), where n is the length of the input array.
        Space complexity: O(n), where n is the length of the input array.
        """
        # Initialize a dictionary to store the frequency of prefix sums
        prefixSum_freq = {0: 1} # Start out with 1 prefixSum equal 0.
        curr_sum = 0
        cnt = 0

        for num in nums:

            curr_sum += num
            comp = curr_sum - k

            # Check if the complement value is present in the prefix sum frequency
            # If so, increment the counter by the frequency of the complement value
            if comp in prefixSum_freq:
                cnt += prefixSum_freq[comp]

            if curr_sum not in prefixSum_freq:
                prefixSum_freq[curr_sum] = 0
            prefixSum_freq[curr_sum] += 1

        return cnt
