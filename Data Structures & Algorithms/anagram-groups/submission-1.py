from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list);
        result = [];

        for s in strs:
            new_word = tuple(sorted(s));
            arr[new_word].append(s);

        for values in arr.values():
            result.append(values);

        return result;
        

            
        
