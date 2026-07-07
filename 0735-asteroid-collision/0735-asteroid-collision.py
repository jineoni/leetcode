class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0
        while i < len(asteroids):
            a = asteroids[i]

            # case: no prev asteroid or no intersection
            if len(st) == 0 or st[-1] < 0 or a > 0:
                st.append(a)
                i += 1
                continue

            # crt bigger than prev -> prev breaks, crt stays
            if abs(a) > st[-1]:
                st.pop()
            # crt equal with prev -> both crt and prev break
            elif abs(a) == st[-1]:
                st.pop()
                i += 1
            # crt smaller than prev -> crt breaks, prev stays
            elif abs(a) < st[-1]:
                i += 1
        
        return st