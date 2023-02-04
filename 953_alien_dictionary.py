class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        is_sorted = True
        order_map = {}

        for i in range(len(order)):
            order_map[order[i]] = i+1
        
        def compare_arrays(arr1,arr2):
            small_len = min(len(arr1),len(arr2))

            for i in range(small_len):
                if arr1[i] > arr2[i]:
                    return False
                elif arr1[i] < arr2[i]:
                    return True
                elif arr1[i] == arr2[i]:
                    continue
            if len(arr1) <= len(arr2):
                return True
            else:
                return False

           

        def check_words(word1,word2):
            word1_arr = []
            word2_arr = []

            for letter in word1:
                word1_arr.append(order_map[letter])
            for letter in word2:
                word2_arr.append(order_map[letter])
            
            return compare_arrays(word1_arr,word2_arr)
            
        for i in range (1,len(words)):
            previous = words[i-1]
            current = words[i]

            check_order = check_words(previous,current)

            if check_order:
                continue
            else:
                is_sorted = False
                break
        return is_sorted
