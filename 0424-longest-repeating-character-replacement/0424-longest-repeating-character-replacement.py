class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        # corner case: k == 0
        # perform regular sliding windows (no character swapping)
        if k == 0:
            return self.regularSlidingWindow(s)
        
        res = 0
        unique_chars = set(s)
        for char in unique_chars:
            left, right = 0, 1
            score = 1
            changes = k - int(s[left] != char)
            while right < len(s):
                if s[right] == char or changes > 0:
                    # expand window
                    if s[right] != char:
                        changes -= 1
                    right += 1
                    score += 1
                    
                    # update res
                    res = max(res, score)
                else:
                    # shrink window
                    if s[left] != char:
                        changes += 1
                    left += 1
                    score -= 1
        return res
    
    def regularSlidingWindow(self, s):
        '''
        return longest substring
        '''
        left, right = 0, 1
        res = 1
        cur_count = 1
        cur_char = s[0]
        while right < len(s):
            if s[right] == cur_char:
                cur_count += 1
            else:
                res = max(res, cur_count)
                left = right
                cur_count = 1
                cur_char = s[left]
            right += 1
        res = max(res, cur_count)
        return res