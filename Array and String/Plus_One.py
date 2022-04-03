class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_map = map(str, digits)
        number = int("".join(str_map)) + 1
        return [int(_) for _ in str(number)]