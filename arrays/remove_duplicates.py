# Remove Duplicates from Sorted Array
# Problem: Given a sorted array nums, remove the duplicates in-place such that each unique element appears only once.

# Why it's important: Similar to "Move Zeroes", this problem is a classic example of using a two-pointer technique to modify an array in-place while keeping the time complexity at O(N). It leverages the fact that the array is sorted to solve the problem efficiently.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,1,2]
    k1 = solution.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # Output: 2, [1, 2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = solution.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
    
