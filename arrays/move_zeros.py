class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1

        return nums

if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([0,1,0,3,12]))  # [1, 3, 12, 0, 0]
    print(solution.moveZeroes([0]))           # [0]
    print(solution.moveZeroes([1,0,1]))       # [1, 1, 0]   
    print(solution.moveZeroes([4,2,4,0,0,3,0,5,1,0]))  # [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]