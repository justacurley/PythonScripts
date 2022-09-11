'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use a pointer to keep track of where we need to insert a new numbner
        # iterate through the list, starting at index 1, because we know index0 is unique and the lowest number
        # If the number in the insert pointer does not equal the number before it, update the number at the insert pointer, and move the                 pointer up one
        ptr = 1
        for i in range(len(nums))[1:]:
            if nums[i] != nums[i-1]:
                nums[ptr] = nums[i]
                ptr+=1
        return ptr
                
            

nums = [0,0,1,1,1,2,2,3,3,4]
Solution.removeDuplicates(nums)