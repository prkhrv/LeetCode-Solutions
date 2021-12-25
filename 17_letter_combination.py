class Solution:
    def __init__(self) -> None:
        self.LETTERS = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []

        result = []
        self._find_combination(digits, 0, "", result)
        return result

    def _find_combination(self, digits: str, digit_index: int, current: str, result: list) -> None:
        if digit_index == len(digits):
            result.append(current)
            return

        digit = digits[digit_index]
        letters = self.LETTERS[digit]

        for letter in letters:
            self._find_combination(digits, digit_index+1,
                                   current+letter, result)
