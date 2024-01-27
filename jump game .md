
### Jump Game (Problem #55):

Determine if you can reach the last index of an array.

Approach: 
Use ***a greedy approach***. Iterate through the array, keep track of `the furthest reachable index`, and check if you can reach the end.

```python

def canJump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
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
