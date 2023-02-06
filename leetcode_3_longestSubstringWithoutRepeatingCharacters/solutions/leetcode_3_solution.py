class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring
        ans = 0
        # store char frequency in current substring
        char_map = {}
        # initialize left boundary of current substring
        left = 0

        # iterate over each char in string
        for right, char in enumerate(s):
            # if char has been seen in current substring
            if char in char_map:
                # update left boundary
                left = max(left, char_map[char] + 1)
                
            # update char frequency
            char_map[char] = right
            # update length of longest substring
            ans = max(ans, right - left + 1)

        # return length of longest substring
        return ans

# # Using HashSet and while loop.
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0
#         char_set = set()
        
#         L, R = 0, 0
#         while R < len(s):
#             char = s[R]
            
#             if char in char_set:
#                 char_set.remove(s[L])
#                 L += 1
#             else:
#                 char_set.add(char)
#                 R += 1
            
#             longest = max(longest, R - L)
            
#         return longest