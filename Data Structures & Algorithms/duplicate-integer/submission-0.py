class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False;
        for i in range(len(nums)):
            for j in range(len(nums)):
                print(i, j);
                if (i != j) and (nums[i] == nums[j]):
                    dup = True;
                    return dup;
        return dup;

        