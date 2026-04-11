# Pattern: Hash Map
# Time: O(n)
# Space: O(n)
# Idea: Store complement while iterating
# Trick: Avoid double loop by checking previous values
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store previous values
        visited: dict[int, int] = {}

        for i, num in enumerate(nums):
            # Check if we found the solution
            missing = target - num
            if missing in visited:
                return [visited[missing], i]
            
            # Store visited value
            visited[num] = i

        # No solution was found
        raise Exception("No answer was found")