from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
            counts = Counter(nums)
            return[num for num , count in counts.most_common(k)]
                    
        