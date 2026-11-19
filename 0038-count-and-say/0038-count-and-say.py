class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(s):
            rle = ""
            cnt = 0
            pt = 0
            curr = s[0]
            while pt < len(s):
                if curr == s[pt]:
                    cnt += 1
                else:
                    rle += str(cnt)
                    rle += curr
                    curr = s[pt]
                    cnt = 1
                pt += 1
            rle += str(cnt)
            rle += curr
            return rle
        
        output = "1"
        for _ in range(n-1):
            output = RLE(output)
        
        return output
            
        

