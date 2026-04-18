class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b_true = [False] * len(strs)
        twoarr = []
        new = [''] * len(strs)
        for i in range(len(strs)):
            new[i] = ''.join(sorted(strs[i]))

        for i in range(len(strs)):
            if b_true[i] != True:
                row = []
                row.append(strs[i])
                b_true[i] = True
                for j in range(len(strs)):
                    if (i != j) and (b_true[j] != True):
                        if new[i] == new[j]:
                            b_true[j] = True
                            row.append(strs[j])
                twoarr.append(row)

        return twoarr