class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        if s[0] in ["}", "]", ")"] or (len(s) % 2 == 1):
            return False
        
        for i in range(0, len(s)):
            if s[i] in ["{", "[", "("]:
                stk.append(s[i])
                continue
            
            if s[i] in ["}", "]", ")"] and len(stk) == 0:
                return False

            if (s[i] == "}" and stk[-1] == "{") or (s[i] == "]" and stk[-1] == "[") or (s[i] == ")" and stk[-1] == "("):
                stk.pop()
            else:
                return False
            
        if len(stk) != 0:
            return False
        
        return True