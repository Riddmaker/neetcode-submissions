class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Input validation
        if not nums:
            return -1

        search_index = 0
        signal = "not_started"
        left = 0
        right = len(nums) -1

        for number in nums:

            if signal == "not_started":
                search_index = right// 2
            elif signal == "higher":
                left = search_index + 1
                search_index = (left + right) // 2
            elif signal == "lower":
                right = search_index - 1
                search_index = (left + right) // 2
            else:
                return -1

            if left > right:
                return -1

            if target == nums[search_index]:
                return search_index
            elif target > nums[search_index]:
                signal = "higher"
            elif target < nums[search_index]:
                signal = "lower"
            else:
                return -1

        
        return -1
        