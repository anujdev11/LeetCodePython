class Solution:
    def fib(self, n: int) -> int:
        # calculates fibonacci
        def calFib(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            return calFib(n-1) + calFib(n-2)
        # func call
        return calFib(n)
        