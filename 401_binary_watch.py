class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [str(hours) + ':' + str(minutes).zfill(2)
            for hours in range(12) for minutes in range(60)
            if (bin(hours) + bin(minutes)).count('1') == turnedOn]
        
