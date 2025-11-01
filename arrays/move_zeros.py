"""
283. Move Zeroes

Problem Statement:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?

Algorithm Explanation:
The solution uses a two-pointer approach:
1. Keep track of the position where the next non-zero element should be placed (last_non_zero_found_at)
2. Iterate through the array, and whenever a non-zero element is found, swap it with the element 
   at the last_non_zero_found_at position
3. This ensures all non-zero elements are moved to the front while maintaining their relative order

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using constant extra space
"""

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