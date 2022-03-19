class FreqStack:

    def __init__(self):
        self.freqstackmap, self.freq, self.maxfreq = defaultdict(list), defaultdict(int), 0

    def push(self, val: int) -> None:
        self.freq[val], self.maxfreq = self.freq[val] + 1, max(self.maxfreq, self.freq[val] + 1)
        self.freqstackmap[self.freq[val]].append(val)
        
    def pop(self) -> int:
        val = self.freqstackmap[self.maxfreq].pop()
        if not self.freqstackmap[self.maxfreq]: self.maxfreq -= 1
        self.freq[val] -= 1
        return val
