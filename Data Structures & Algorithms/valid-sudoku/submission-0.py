class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows    = defaultdict(list)
        cols    = defaultdict(list)
        boxes   = defaultdict(list)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                if val in rows[i]:
                    return False
                rows[i].append(val)

                if val in cols[j]:
                    return False
                cols[j].append(val)

                box_key = (i // 3, j // 3)
                if val in boxes[box_key]:
                    return False
                boxes[box_key].append(val)

        return True