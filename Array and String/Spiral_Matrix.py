class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        element = 0
        
        row = len(matrix); column = len(matrix[0])
        row_start = 0; column_start = 0
        row_end = row - 1; column_end = column - 1
        row_index = 0; column_index = 0
        
        result = []
        
        while element != (row * column):
            
            current_element = matrix[row_index][column_index]
            
            result.append(current_element)
            
            if row_index == row_start:
                column_index += 1
                if column_index > column_end:
                    row_index += 1
                    column_index -= 1
            
            elif column_index == column_end:
                row_index += 1
                if row_index > row_end:
                    column_index -= 1
                    row_index -= 1
            
            elif row_index == row_end:
                column_index -=1
                if column_index < column_start:
                    row_index -=1
                    column_index += 1
            
            elif column_index == column_start:
                row_index -= 1
                if row_index == row_start:
                    row_start += 1; row_end -= 1
                    column_start += 1; column_end -=1
                    row_index += 1; column_index += 1
                
            element += 1
            
        return result