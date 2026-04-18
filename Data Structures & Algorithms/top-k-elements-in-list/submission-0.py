class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b_visited = [False] * len(nums);
        twoarr = [];
        finalarr = [];
        output = [];
        for i in range(len(nums)):
            if b_visited[i] != True:
                   
                row = [];
                row.append(nums[i]); 
                b_visited[i]=True;
                for j in range(len(nums)):
                    if (i!=j) and (nums[i] == nums[j]) and (b_visited[j]==False):
                        
                        row.append(nums[j]);
                        b_visited[j]=True;
                twoarr.append(row);

        for m in range(len(twoarr)):
            for l in range(len(twoarr) - m - 1):
                if len(twoarr[l]) < len(twoarr[l+1]):
                    twoarr[l], twoarr[l+1] = twoarr[l+1], twoarr[l];
        
        for b in range(k):
            output.append(twoarr[b][0]);

        return output;