class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ["tarantula","taranasaur","tarantino"]
        # set the prefix to the first string in the list
        # iterate over each string
        # while the current string does not start with prefix, remove the last character of the prefix
         #if the prefix is empty, return an empty string
        prefix = strs[0]        
        print(prefix.startswith('fl'))
        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[0:(len(prefix)-1)]
                print("new pref",prefix)
                if not prefix:
                    return ''
        return prefix