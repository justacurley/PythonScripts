'''
The key to this one is that the current closing character must match the last opening character in the string
We can use a stack to push the new found opening characters, 
and then pop them when we find their matching close, 
or return false if we find a close character that does not match the open character at the top of the stack

( 
^ push onto stack
((
 ^ push onto stack
((]
  ^ check if this closing character has a matching opening character at the top of the stack. It doesn't, so return false
  
( 
^ push onto stack
((
 ^ push onto stack
(()
  ^ check if this closing character has a matching opening character at the top of the stack. It does, so pop the top of the stack
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openc =  [ '[', '{', '(' ]
        closec = [ ']', '}', ')' ]
        open_close = dict(zip(closec,openc))    
        for c in s:
            if c in closec:
                # print("stack[-1] == open_close[c]",stack[-1] == open_close[c])
                if len(stack) > 0 and stack[-1] == open_close[c]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else: return False

strin = ']'
# strin = '()()'
task = Solution()
answer = task.isValid(strin)
print(answer)
# Solution.isValid(strin)