
class Day2:

    def survivor(self, n, k):
        if n == 1:
            return 0
        else:
            """
            Winner of (n,k) = Winner of (n-1,k) + k 
            Example : (5,3)
            [1,2,3,4,5]
            [1,2,-,4,5]
            [-,2,-,4,5]
            [-,2,-,4,-]
            [-,-,-,4,-]
            
            (4,3)+3
            [1,2,-,4] + 3
            [1,4] + 3
            [1] +3
            [4]
            """
            return (self.survivor(n-1, k) + k) % n







