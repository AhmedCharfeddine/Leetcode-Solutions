class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_rows():
            for row in board:
                nums = [n for n in row if n != '.']
                if len(nums) != len(set(nums)):
                    return False
            return True
                
        def check_columns():
            for i in range(len(board[0])):
                column = [board[j][i] for j in range(len(board)) if board[j][i] != '.']
                if len(column) != len(set(column)):
                    return False
            return True
                
        def check_squares():
            squares_start = [
                (0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6),
            ]
            squares_end = [
                (2, 2), (2, 5), (2, 8),
                (5, 2), (5, 5), (5, 8),
                (8, 2), (8, 5), (8, 8),
            ]
            
            for square in zip(squares_start, squares_end):
                coord = range(square[0][0], square[1][0] + 1), range(square[0][1], square[1][1] + 1)
                cur_square = [board[i][j] for i in coord[0] for j in coord[1] if board[i][j] != '.']
                if len(cur_square) != len(set(cur_square)):
                    return False
            return True
                
        return all([check_rows(), check_columns(), check_squares()])