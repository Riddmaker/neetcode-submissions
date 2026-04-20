class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            false

        lp = 0 
        rp = len(s) - 1
        vl = 0
        vr = 0
        vl_filled = False
        vr_filled = False

        while lp < rp:
            if s[lp].isalnum():
                vl = s[lp].lower()
                vl_filled = True
            else:
                vl_filled = False
                lp += 1

            if s[rp].isalnum():
                vr = s[rp].lower()
                vr_filled = True
            else:
                vr_filled = False
                rp -= 1

            if vl_filled and vr_filled:
                if vl == vr:
                    lp += 1
                    rp -= 1
                    continue
                else:
                    return False
            else:
                continue
        
        return True


        