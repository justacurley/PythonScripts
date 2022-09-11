from typing import List
from collections import deque


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Task: 

        Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of 
        American keyboard like the image below.

        In the American keyboard:

        the first row consists of the characters "qwertyuiop",
        the second row consists of the characters "asdfghjkl", and
        the third row consists of the characters "zxcvbnm".

        Examples:
            Example 1:
            Input: words = ["Hello","Alaska","Dad","Peace"]
            Output: ["Alaska","Dad"]

            Example 2:
            Input: words = ["omk"]
            Output: []

            Example 3:
            Input: words = ["adsdf","sfd"]
            Output: ["adsdf","sfd"]

        There is only one occurrence of each character in the kb rows.
        A -> row2 laska has to be in row 2 or its false  

        keep track of current row in current_row, declare current_row as -1 or None or whatever 
        for word in words:   
        iterate the letters in the Word
         is current_row set?
          No. look up the row for the letter in thisset
           update current_row, and now all further iterations only look for the letter in that row
          Yes. is current letter in current_row? If no, break out of loop for this word
        add Word to answer and set current_row back to -1 or none of whatever
        """
        letter_map = {
            "q": 0,
            "w": 0,
            "e": 0,
            "e": 0,
            "r": 0,
            "t": 0,
            "y": 0,
            "u": 0,
            "i": 0,
            "o": 0,
            "p": 0,
            "a": 1,
            "s": 1,
            "d": 1,
            "f": 1,
            "g": 1,
            "h": 1,
            "j": 1,
            "k": 1,
            "l": 1,
            "z": 2,
            "x": 2,
            "c": 2,
            "v": 2,
            "b": 2,
            "n": 2,
            "m": 2
        }
        row_map = {
            0: {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"},
            1: {"a", "s", "d", "f", "g", "h", "j", "k", "l"},
            2: {"z", "x", "c", "v", "b", "n", "m"}
        }

        # keep track of current row in current_row, declare current_row as -1 or None or whatever
        # for word in words:
        # iterate the letters in the Word
        #  is current_row set?
        #   No. look up the row for the letter in thisset
        #    update current_row, and now all further iterations only look for the letter in that row
        #   Yes. is current letter in current_row? If no, break out of loop for this word
        # add Word to answer and set current_row back to -1 or none of whatever

        # answer=words.copy()
        answer = []
        for i in range(len(words)):
            word = words[i].lower()
            current_row = letter_map[word[0]]
            remove = False
            for letter in word:
                if letter not in row_map[current_row]:
                    remove = True
                    break
            if remove == False: answer.append(words[i])
        return answer
            

    def testTask(self, nums=List[int], answer=[int]) -> bool:
        test_cases = {
            0: {
                "Input": ["Hello", "Alaska", "Dad", "Peace"],
                "Output": ["Alaska", "Dad"]
            },
            1: {
                "Input": ["omk"],
                "Output": []
            },
            2: {
                "Input": ["adsdf", "sfd"],
                "Output": ["adsdf", "sfd"]
            },
            3: {
                "Input": ["asdfghjkl","qwertyuiop","zxcvbnm"],
                "Output": ["asdfghjkl","qwertyuiop","zxcvbnm"]
            }
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.findWords(test_cases[i]["Input"])
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
