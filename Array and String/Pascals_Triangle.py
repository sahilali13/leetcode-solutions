class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for line in range(1, numRows + 1):
            temp = []
            C = 1
            for _ in range(1, line + 1):
                temp.append(C)
                C = int(C * (line - _) / _)
            result.append(temp)
        return result