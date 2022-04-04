class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = [mat[0][0]]
        
        row = len(mat)
        column = len(mat[0])
        
        column_start = 1
        
        counter = 1
        
        while column_start != column:
            column_index = column_start
            temp = []
            row_index = 0
            
            while column_index != -1 and row_index < row:
                temp.append(mat[row_index][column_index])
                row_index +=1
                column_index -=1
            
            counter += 1
            if counter % 2 != 0:
                temp.reverse()
            
            column_start += 1
            result += temp
        
        row_start = 1
        
        while row_start != row:
            column_index = column - 1
            temp = []
            row_index = row_start
            while row_index != row and column_index >= 0:
                temp.append(mat[row_index][column_index])
                row_index += 1
                column_index -=1
            
            counter += 1
            if counter % 2 != 0:
                temp.reverse()
            row_start += 1
            result += temp
            
        return result
                