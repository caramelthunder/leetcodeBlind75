class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_element = None
        count = 0

        for num in nums:
            if count == 0 or majority_element == num:
                majority_element = num
                count += 1
            elif majority_element != num:
                count -= 1

        return majority_element if count > 0 else None

        # # Boyer-Moore Majority Vote algorithm ##
        # for num in nums:
        #     if count == 0:
        #         majority_element = num
        #     count += (1 if majority_element == num else -1)
        
        # return majority_element