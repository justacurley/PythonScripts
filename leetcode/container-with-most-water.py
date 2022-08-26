from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Task: 
            You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
            Find two lines that together with the x-axis form a container, such that the container contains the most water.
            Return the maximum amount of water a container can store.
            Notice that you may not slant the container.

            Algorithm

            The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. 
            Farther the lines, the more will be the area obtained.

            We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. 
            Futher, we maintain a variable \text{maxarea}maxarea to store the maximum area obtained till now. 
            At every step, we find out the area formed between them, update \text{maxarea}maxarea and move the 
            pointer pointing to the shorter line towards the other end by one step.

            The algorithm can be better understood by looking at the example below:

            1 8 6 2 5 4 8 3 7
            Current
            1 / 8
            How does this approach work?

            Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider 
            the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain
            any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out 
            to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer 
            line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.

        Examples:
            Example 1:
            Input: height = [1,8,6,2,5,4,8,3,7]
            Output: 49
            Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

            Example 2:
            Input: height = [1,1]
            Output: 1
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            distance = right - left
            lower = min(height[right], height[left])
            area = distance*lower
            max_area = max(max_area, area)
            if lower == height[right]:
                right -= 1
            else:
                left += 1

        return max_area

    def testTask(self):
        test_cases = {
            0: {
                "Input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
                "Output": 49
            },
            1:
            {
                "Input": [1, 1],
                "Output": 1
            }
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.maxArea(test_cases[i]["Input"])
            if test_cases[i]["Output"] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[i]["Output"])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[i]["Output"])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
