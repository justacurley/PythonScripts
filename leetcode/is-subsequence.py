class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two for loops?
         # for x abc
            # for y ahbgdc
             # we are looking for x == y, and maybe the index?
             # if the next for x has an index greater than the previous iteration, store it and continue
             # if the next for x has no index, or an index less than the previous iteration, it fails
        # last_index = 0
        # for i_s in range(len(s)):
        #     for i_t in range(len(t)):
        #         if (s[i_s] == t[i_t]):
        #             print(i_t > last_index)
        #             last_index = i_t
                    # This works except if the first match is at index 0, not sure an efficient way to check that

        # This is much better
        # for c in abc
         # use the find() method to get index of c in t, starting at the last known good index
         #    then add 1 to that to ensure you are starting from the last known good index
        position = 0
        for c in s:
            position = t.find(c, position)+1
            if (position == 0):
                return False
        return True