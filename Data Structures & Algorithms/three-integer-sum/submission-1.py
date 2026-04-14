class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        n = len(nums)

        for i in range(n):

            # Continue on duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1        
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                # Solution found
                if total == 0:
                    solutions.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Move on duplicate
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return solutions