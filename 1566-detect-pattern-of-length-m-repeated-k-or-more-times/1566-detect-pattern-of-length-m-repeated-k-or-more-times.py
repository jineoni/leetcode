class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        cnt = 0
        for i in range(len(arr)-m):
            if arr[i] == arr[i+m]:
                cnt += 1
            else:
                cnt = 0
            if cnt == m * (k-1):
                return True
        return False
