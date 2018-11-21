MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31
class Solution(object):
    def myAtoi(self, stri):
        """
        :type str: stri
        :rtype: int
        """
        start = 0
        n = len(stri)

        # skip white space
        while start < n and stri[start] == ' ':
            start += 1

        if start >= n:
            return 0

        sign = 1
        nums = map(str, range(10))
        start_set = {'-', '+'} | set(nums)
        if stri[start] not in start_set:
            return 0

        elif stri[start] == '-':
            start += 1
            sign = -1
        elif stri[start] == '+':
            start += 1
            sign = 1

        end = start

        while end < n and stri[end].isdigit():
            end += 1

        if start >= end:
            return 0

        ans = sign * int(stri[start:end])

        if ans < MIN_INT:
            return MIN_INT
        if ans > MAX_INT:
            return MAX_INT

        return ans