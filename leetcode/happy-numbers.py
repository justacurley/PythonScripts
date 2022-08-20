

class Solution:
    """
    Write an algorithm to determine if a number n is happy.
    A happy number is a number defined by the following process.
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.

    Example 1:
    Input: n = 19
    Output: true
    Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

    Example 2:
    Input: n = 2
    Output: false 

    Constraints:
    1 <= n <= 231 - 1
    """

    def getSquaredVal(self,s:str)->int:
        sum_power = 0
        for i in range(len(s)):
            digit = int(s[i])
            sum_power += int(digit**2)
        return sum_power



    def isHappy(self, n: int) -> bool:
        """
        answer = False
        Calculates number
        Convert int to str, "the_string"
        storage set, "found_numbers"   
        storage int, "sum_power"   
        while sum_power ne 1
            for ea. s in the_string
                convert to int and square number, "squared"                
                add squared to storage var sum_power
            add sum_power to found_numbers
            if sum_power in found_numbers
                answer = False
                break
        answer = True
        return answer
        """
        the_string = str(n)
        found_numbers = set()
        while True:
            sum_power = self.getSquaredVal(the_string)
                
            if sum_power in found_numbers:
                return False

            if sum_power == 1:
                return True
            
            found_numbers.add(sum_power)
            the_string = str(sum_power)
            


                
    def testTask(self) -> bool:
        test_cases = {
            19: True,
            2: False
        }
        passed = 0
        failed = 0
        for key in test_cases:
            code_answer = self.isHappy(key)
            if test_cases[key] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[key])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[key])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
