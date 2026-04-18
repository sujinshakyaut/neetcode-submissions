class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                total = 0;
                total = nums[i]+nums[j];
                if (i!=j) and total==target:
                    if i<j:
                        ret_arr = [i,j];
                    else:
                        ret_arr = [j,i];
                    return ret_arr;

            
