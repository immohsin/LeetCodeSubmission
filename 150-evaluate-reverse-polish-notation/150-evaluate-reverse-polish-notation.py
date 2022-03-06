
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operands = {'+','-', '*', '/'}
        for i in tokens:
            if i in operands:
                val1 = s.pop()
                val2 = s.pop()
                s.append(int(eval("{0} {1} {2}".format(val2, i, val1))))
            else:
                s.append(i)
        return s[0]