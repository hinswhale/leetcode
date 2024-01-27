
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
Complexity Analysis:

Time Complexity: O(n)
The algorithm iterates through the array once, where n is the length of the array.

Space Complexity: O(1)
The algorithm uses only a constant amount of extra space, regardless of the size of the input array.


### Jump Game II (Problem #45):（https://leetcode.com/problems/jump-game-ii/）

Find the minimum number of jumps to reach the last index.
Approach: Use ***a greedy approach***. Instead of checking if you can reach the end, find the minimum number of jumps required to reach each position.
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans,farthest,end = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            print(i, farthest, ans)
            if i == end:
                ans += 1
                end = farthest
        return ans

```

Complexity Analysis:

Time Complexity: O(n)
The algorithm iterates through the array once, where n is the length of the array.

Space Complexity: O(1)
The algorithm uses only a constant amount of extra space, regardless of the size of the input array.

### Jump Game III (Problem #1306):

Determine if it is possible to reach the last index starting from an array of non-negative integers.
Approach: Use ***DFS (Depth-First Search)*** or ***BFS (Breadth-First Search)*** to explore all possible paths and check if you can reach the last index.

> warning:  be stuck in an infinite loop

> recursion

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def is_valid(index):
            return  0 <= index < n 

        n = len(arr)
        visited = set()

        def Reach(num):
            if  not is_valid(num) or num in visited:
                return False
            
            if arr[num] == 0:
                return True
            
            visited.add(num)
            return Reach(num - arr[num]) or Reach(num + arr[num])
        
        return Reach(start)
```

> Breadth-First Search (BFS) using deque
```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def is_valid(index):
            return  0 <= index < n 
        
        n = len(arr)

        queue = [start]
        visited = set()

        while queue:
            new_q = []
            for i in queue:
                visited.add(i)
                if arr[i] == 0:
                    return True
            
            for i in queue:
                ls = i - arr[i]
                rs = i + arr[i]
                
                if is_valid(ls) and ls not in visited: 
                    visited.add(ls)
                    new_q.append(ls)
                
                if is_valid(rs) and rs not in visited: 
                    visited.add(rs)
                    new_q.append(rs)
            queue = new_q
            
        return False

```
Complexity Analysis:

Time Complexity: O(n)
The algorithm uses BFS to traverse the array, visiting each element at most twice.

Space Complexity: O(n)
The algorithm uses a set to keep track of visited indices and a deque for the BFS queue. In the worst case, all elements might be visited, so the space complexity is O(n).

###  Jump Game IV (Problem #1345):

Find the minimum number of steps to reach the last index in an array of integers.

### Jump Game V (Problem #1340):

Determine the maximum number of steps you can take starting from each index in an array.

### Frog Jump (Problem #403):

Determine if the frog can cross a river given a list of stones where each stone represents a jump distance.
