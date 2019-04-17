class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # find first nums[i] < nums[j]
        n = len(nums)
        i=0
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                break
            else:
                return nums[::-1]

        for j in range(n-1, i, -1):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
        nums[i+1:] = reversed(nums[i+1:])
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.nextPermutation([1,2,3]))