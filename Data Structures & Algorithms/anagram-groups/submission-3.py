class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        anagram_buckets = {}
        

        for s in strs:
            sig = [0] * 26

            for c in s:
                
                idx = ord(c) - ord('a')

                sig[idx] += 1
            
            sig = tuple(sig)
            
            if sig not in anagram_buckets:
                anagram_buckets[sig] = [s]
            else:
                anagram_buckets[sig].append(s)
        
        return list(anagram_buckets.values())