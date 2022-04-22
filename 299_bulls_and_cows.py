class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0
        secret_dict = Counter(secret)
        guess_dict = Counter(guess)
        
        count = 0
        for k,v in secret_dict.items():
            if k in guess_dict:
                count+=min(secret_dict[k],guess_dict[k])
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls+=1
        
        cows = abs(count-bulls)
        return str(bulls)+"A"+str(cows)+"B"
