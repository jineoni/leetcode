class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return s

        currNum = 0
        intStack = []
        strStack = []

        for x in s:
            if x.isdigit():
                currNum = (currNum * 10) + int(x)
            else:
                if x == '[':
                    intStack.append(currNum)
                    currNum = 0
                    strStack.append(x)
                elif x == ']':
                    temp = ""
                    while strStack and strStack[-1] != '[':
                        temp = strStack.pop() + temp
                    strStack.pop() # [ 제거
                    num = intStack.pop()
                    strStack.append(temp * num)
                else:
                    strStack.append(x)
        
        return "".join(strStack)
            