class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        MIN, MAX = -2**31, 2**31 - 1
        is_negative= False

        # Skip over empty spaces.
        i = 0
        while i < n and s[i] == " ":
            i += 1
        # Handle negative sign.
        if i < n and s[i] in ["-", "+"]:
            is_negative = (s[i] == '-')
            i += 1

        num = 0
        while i < n:
            char = s[i]

            if not char.isdigit():
                break
            else:
                if (num < MAX // 10) or (num == MAX // 10 and int(char) <= MAX % 10):
                    num = num * 10 + int(char)
                    i += 1
                else:
                    return MIN if is_negative else MAX
            
        return -num if is_negative else num