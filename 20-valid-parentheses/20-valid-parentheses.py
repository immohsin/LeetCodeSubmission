class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False
        st = []
        for i in s:
            if i in '([{':
                st.append(i)
            else:
                if i == ')':
                    if not st or (len(st) and st[-1] != '('):
                        return False
                    st.pop()
                elif i == ']':
                    if not st or (len(st) and st[-1] != '['):
                        return False
                    st.pop()
                elif i == '}':
                     if not st or (len(st) and st[-1] != '{'):
                        return False
                     st.pop()
        return False if len(st) else True
        