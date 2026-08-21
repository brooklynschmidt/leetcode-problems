class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        
# bottom up solution, no recursion:
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                cache[i] = 1
            elif i == 2:
                cache[i] = 2
            else:
                cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
