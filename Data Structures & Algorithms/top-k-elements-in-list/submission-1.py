from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = defaultdict(list);
        keys = [];
        
        for n in range(len(nums)):
            arr[nums[n]].append(nums[n]);
        
        for n in arr:
            keys.append(n);


        for i in range(len(keys)):
            for j in range(len(keys) - i - 1):
                if len(arr[keys[j]]) < len(arr[keys[j+1]]):
                    keys[j], keys[j+1] = keys[j+1], keys[j]
        
        return keys[:k]
            
            
