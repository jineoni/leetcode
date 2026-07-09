class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                string = ""
                while stack:
                    letter = stack.pop()
                    if letter == '[':
                        continue
                    elif letter.isdigit():
                        num = letter
                        while stack and stack[-1].isdigit():
                            num = stack.pop() + num
                        for _ in range(int(num)):
                            for j in range(len(string)):
                                stack.append(string[::-1][j])
                        # stack.append(string[::-1] * int(num))
                        break
                    else:
                        string += letter
            else:
                stack.append(s[i])
        return "".join(stack)