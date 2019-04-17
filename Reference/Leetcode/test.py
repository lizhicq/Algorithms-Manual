class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] == val:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                hi -= 1
            else:
                lo += 1
        return hi+1

if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([1,3,3],3))