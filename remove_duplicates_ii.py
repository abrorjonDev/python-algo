# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

"""
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:

        Input: nums = [1,1,1,2,2,3]
        Output: 5, nums = [1,1,2,2,3,_]
        Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:

        Input: nums = [0,0,1,1,1,1,2,3,3]
        Output: 7, nums = [0,0,1,1,2,3,3,_,_]
        Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).


"""

# 54ms time and 16.33mb
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        step, count = 0, 1

        while step < len(nums) - 1:
            if nums[step] == nums[step + 1]:
                if count < 2:
                    step += 1
                    count += 1
                else:
                    del nums[step]
            else:
                step += 1
                count = 1
        return len(nums)


# 52ms time and 16.14mb
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        index: int = 0

        while index < len(nums) - 2:
            if nums[index] == nums[index + 2]:
                del nums[index]
            else:
                index += 1

        return len(nums)


if __name__ == '__main__':
    a = Solution1()

    assert a.removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7
    assert a.removeDuplicates([1,1,1,2,2,3]) == 5
    assert a.removeDuplicates([1,1,1,2,2,3,3,3,4,4]) == 8

    a = Solution2()

    assert a.removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7
    assert a.removeDuplicates([1,1,1,2,2,3]) == 5
    assert a.removeDuplicates([1,1,1,2,2,3,3,3,4,4]) == 8
