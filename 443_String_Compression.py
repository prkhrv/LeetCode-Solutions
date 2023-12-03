class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        current_count = 1
        left = 1

        for i in range(1,len(chars)):
            if chars[i] == current:
                current_count+=1
                continue
            else:
                if current_count == 1:
                    current = chars[i]
                    chars[left] = current
                    left+=1
                    
                else:
                    str_count = str(current_count)
                    for ch in str_count:
                        chars[left] = ch
                        left+=1
                    current_count = 1
                    current = chars[i]
                    chars[left] = current
                    left+=1
        
        if current_count == 1:
            return left
        else:
            str_count = str(current_count)
            for ch in str_count:
                chars[left] = ch
                left+=1
            return left
