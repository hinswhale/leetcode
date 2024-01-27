
### Jump Game (Problem #55):

Determine if you can reach the last index of an array.

Approach: 
Use ***a greedy approach***. Iterate through the array, keep track of `the furthest reachable index`, and check if you can reach the end.

```python

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(n-1):
            max_reach = max(ans, i + nums[i]) # 目前能到达的最远index
            if max_reach <= i: # 最远index 没有超过下标的速度，说明被卡了
                return False 
        return True

```

### Jump Game II (Problem #45):

Find the minimum number of jumps to reach the last index.

### Jump Game III (Problem #1306):

Determine if it is possible to reach the last index starting from an array of non-negative integers.

###  Jump Game IV (Problem #1345):

Find the minimum number of steps to reach the last index in an array of integers.

### Jump Game V (Problem #1340):

Determine the maximum number of steps you can take starting from each index in an array.

### Frog Jump (Problem #403):

Determine if the frog can cross a river given a list of stones where each stone represents a jump distance.
