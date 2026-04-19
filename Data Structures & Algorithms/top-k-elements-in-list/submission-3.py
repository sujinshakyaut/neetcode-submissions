from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = defaultdict(list);
        keys = [];
        
        for n in range(len(nums)):
            arr[nums[n]].append(nums[n]);
        
  
        return heapq.nlargest(k, arr.keys(), key=lambda x: len(arr[x]))
            
            
