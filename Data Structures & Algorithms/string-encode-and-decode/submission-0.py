class Solution:
    def encode(self, strs: List[str]) -> str:
        newString = ""
        for word in strs:
            newString += str(len(word)) + "#" + word
            
        return newString
    def decode(self, s: str) -> List[str]:
        ans = []
        i, j = 0, 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            start = j + 1
            end = start + length 
            ans.append(s[start:end])
            i = end
            j = i
        
        return ans
        
