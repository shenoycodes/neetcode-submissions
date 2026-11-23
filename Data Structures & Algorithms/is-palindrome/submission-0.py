class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_clean = ""

        for i in s:
            if i.isalnum():
                s_clean+=i.lower()
                        
        print("s_clean:",s_clean)
        
        for j in range(len(s_clean)):
            if (s_clean[j]!=s_clean[len(s_clean)-j-1]):
                return False
        
        return True

