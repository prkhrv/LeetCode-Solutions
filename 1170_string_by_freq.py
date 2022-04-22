class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        list_of_queries = []
        list_of_words = []
        for query in queries:
            d = Counter(query)[min(query)]
            list_of_queries.append(d)
        
        for word in words:
            w = Counter(word)[min(word)]
            list_of_words.append(w)
        
        for q in list_of_queries:
            flag = 0
            for w in list_of_words:
                if q < w:
                    flag+=1
            
            ans.append(flag)
        return ans
