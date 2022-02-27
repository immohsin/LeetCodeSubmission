# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            num = start + (end - start)  // 2
            g = guess(num)
            if g == 0:
                return num
            elif g == 1:
                start = num + 1
            else:
                end = num - 1