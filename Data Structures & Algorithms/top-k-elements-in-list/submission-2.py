from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = defaultdict(list);
        keys = [];
        
        for n in range(len(nums)):
            arr[nums[n]].append(nums[n]);
        
        for n in arr:
            keys.append(n);


        def quicksort(keys):
            if len(keys) <= 1:
                return keys
            pivot = keys[len(keys) // 2]
            left  = [x for x in keys if len(arr[x]) > len(arr[pivot])]
            mid   = [x for x in keys if len(arr[x]) == len(arr[pivot])]
            right = [x for x in keys if len(arr[x]) < len(arr[pivot])]
            return quicksort(left) + mid + quicksort(right)
        
        keys = quicksort(list(arr.keys()))
        
        return keys[:k]
            
            
