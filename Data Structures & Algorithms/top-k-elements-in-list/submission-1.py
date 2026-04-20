class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Prepare empty hashmap. 
        count = {}
        # Prepare frequency array, based on length of nums.
        freq = [[] for i in range(len(nums) + 1)]
        # Prepare result array.
        res = []
        # Iterate through nums.
        for num in nums:
            # Add + 1 to the counter for the currently encountered number.
            count[num] = 1 + count.get(num, 0)
        # Iterate through key value pairs in count.
        for n, c in count.items():
            freq[c].append(n)
        # Iterate through reduced length frequency array in descending order
        for i in range(len(freq) - 1, 0, -1):
            # Iterate through numbers array in current frequency bucket
            for n in freq[i]:
                # Append found numbers to result
                res.append(n)
                # When result reached the same size as k, return the result.
                if len(res) == k:
                    return res