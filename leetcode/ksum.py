class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target
        You may return the answer in any order.

        Example 1:

        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        Example 2:
        Input: nums = [2,2,2,2,2], target = 8
        Output: [[2,2,2,2]]
        """

        def kSum(nums: list[int], target: int, k: int) -> list[list[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            res = []
            s = set()

            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return res

        nums.sort()
        return kSum(nums, target, 4)


    def testTask(self):
        test_cases = {
            0: {
                "Input": {
                    "nums": [1,0,-1,0,-2,2],
                    "target":0
                },
                "Output": [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
            },
            1: {
                "Input": {
                    "nums": [2,2,2,2,2],
                    "target": 8
                },
                "Output": [[2,2,2,2]]
            },
            2: {
                "Input": {
                    "nums": [2,2,2,2,2],
                    "target": 8
                },
                "Output": [[2,2,2,2]]
            },
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.fourSum(test_cases[i]["Input"]["nums"],test_cases[i]["Input"]["target"])
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
