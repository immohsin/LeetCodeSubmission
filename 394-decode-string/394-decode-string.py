class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for i in s:
            if i.isdigit() or i >= 'a' and i <= 'z' or i == '[':
                stack.append(i)
            
            if i == ']':
                t, num_str = '', ''
                while stack:
                    c = stack.pop()
                    if c == '[':
                        break
                    t = c + t
                while stack and stack[-1].isdigit():    
                    n = stack.pop()
                    num_str= n + num_str
                stack.append(int(num_str) * t)
        return ''.join(stack)
            