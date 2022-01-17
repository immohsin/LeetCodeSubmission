def get_nlr(arr):
    nlr = [-1] * len(arr)
    s = []
    for i in range(len(arr)):
        while len(s) and arr[s[-1]] < arr[i]:
            idx = s.pop()
            nlr[idx] = i
        s.append(i)
    return nlr

def get_nll(arr):
    s = []
    nll = [-1] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        while len(s) and arr[s[-1]] < arr[i]:
            idx = s.pop()
            nll[idx] = i
        s.append(i)
    return nll
            
    
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        nlr = get_nlr(seats)
        nll = get_nll(seats)
        res = 0
        for i in range(len(nlr)):
            if seats[i] == 0:
                if nlr[i] != -1 and nll[i] != -1:
                    ele =  min(abs(i-nlr[i]), abs(i- nll[i]))
                elif nll[i] == -1:
                    ele = abs(i - nlr[i])
                else:
                    ele = abs(i - nll[i])
                res = max(res,ele)
        return res