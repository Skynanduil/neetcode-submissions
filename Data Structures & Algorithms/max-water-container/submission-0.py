class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointer
        # Store max_area and keep moving it, finally return the max area

        left = 0
        right = len(heights) - 1
        total = 0

        while left < right:
            new_total = min(heights[left], heights[right]) * (right - left)
            if new_total > total:
                total = new_total
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return total