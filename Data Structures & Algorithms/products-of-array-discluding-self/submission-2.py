class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            product = 1
            for k in range(len(nums)):
                if k != i:
                    product = product * nums[k]
            arr.append(product)
        return arr