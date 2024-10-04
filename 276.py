    """
    276. Paint Fence
    
    You are painting a fence of n posts with k different colors. You must paint
    the posts following these rules:
    
    - Every post must be painted exactly one color.
    - There cannot be three or more consecutive posts with the same color.
    
    Given the two integers n and k, return the number of ways you can paint the
    fence.
    """
    
    INT_MAX = (1 << 31) - 1
    
    
    class Solution:
        def numWays(self, n: int, k: int) -> int:
            def calc_way(n: int, streak: int, prev_color: int) -> int:
                nonlocal k
    
                if n == 0:
                    return 1
    
                ways = 0
    
                for color in range(k):
                    if color == prev_color:
                        if streak == 2:
                            ways += calc_way(n - 1, 1, color)
                        else:
                            ways += calc_way(n - 1, streak + 1, prev_color)
                    else:
                        ways += calc_way(n - 1, 1, color)
    
                return ways
    
            return calc_way(n, 0, -1)
