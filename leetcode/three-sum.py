from typing import List

class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    aka we can't reuse index value

    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
    Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Returns lists of numbers adding up to 0
        """
        """"
        Sort the given array.
        Loop over the array and fix the first element of the possible triplet, arr[i].
        Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum, 
        If the sum is smaller than the required sum, increment the first pointer.
        Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
        Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.

        [-4, -1, -1, 0, 1, 2]
        -4 + -1
        -5 
        """
        nums.sort()
        first_triplet = int()
        answer = List
        
        for i in range(len(nums)-1):
            left_pointer = i + 1
            right_pointer = len(nums)-1
            first_triplet = nums[i]
            
            while (left_pointer < right_pointer):
                first_triplet + nums[left_pointer] + nums[right_pointer] 
                
                if (first_triplet + nums[left_pointer] + nums[right_pointer] == 0):
                    print("adds to 0", first_triplet, nums[left_pointer], nums[right_pointer])
                    answer.append([first_triplet, nums[left_pointer], nums[right_pointer]])

                elif ( first_triplet + nums[left_pointer] + nums[right_pointer] < 0 ):
                    left_pointer += 1
                
                elif ( first_triplet + nums[left_pointer] + nums[right_pointer] > 0 ):
                    right_pointer -= 1
            
            if (answer):
                print ("Answer was true: ", answer)
                return answer
            else:
                return False


    def testTask(self):
        test_cases = {
            0: {
                "Input": [-1, 0, 1, 2, -1, -4],
                "Output": [[-1, -1, 2], [-1, 0, 1]]
            },
            1: {
                "Input": [0, 1, 1],
                "Output": []
            },
            2: {
                "Input": [0, 0, 0],
                "Output": [[0, 0, 0]]
            }
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.threeSum(test_cases[i]["Input"])
            if test_cases[i] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[i])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[i])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed / (passed + failed)) * 100,
              "%")


task = Solution()
answer = task.testTask()