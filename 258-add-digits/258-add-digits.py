class Solution:
    def addDigits(self, num: int) -> int:
        while num and num > 9:
            num = addNum(num)
        return num
        

def addNum(num):
    ans = 0
    while num:
        ans+=(num%10)
        num = num // 10
    return ans