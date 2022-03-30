class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        i = 0
        while i < len(chars):
            occ = 1
            while i+1 < len(chars) and chars[i] == chars[i+1]:
                occ+=1
                i+=1
            res.append(chars[i])
            if occ > 1:
                res.extend(list(str(occ)))
            i+=1
        chars[:] = res
        return len(chars)