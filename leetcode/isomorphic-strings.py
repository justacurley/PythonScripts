class Solution:
     def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(s)):
            # if s[i] is already in the dict but map[s[i]] ne t[i], then we have a second ocurrence of s[i] with a different value at index t[i]
            if s[i] in map.keys():
                if map[s[i]] != t[i]:
                    return False
            else:
                # has t[i] been added as a value for a different s[i]
                if t[i] in map.values():
                    return False
                map[s[i]]=t[i]
        return True