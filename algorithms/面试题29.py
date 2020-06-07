# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(len(matrix) == 0):
            return []
        matrix_row_num = len(matrix)
        matrix_col_num = len(matrix[0])
        min_num = min(matrix_row_num, matrix_col_num)
        sum_level = (min_num + 1) >> 1
        cur_level = 0
        res = []
        while(cur_level < sum_level):
            self.add_data(matrix, cur_level, matrix_row_num-2 *
                          cur_level, matrix_col_num-2*cur_level, matrix_row_num,matrix_col_num,res)
            cur_level += 1
        return res

    def add_data(self, matrix, level, row_num, col_num,matrix_row_num,matrix_col_num, res):
        # 当前最后一列的下标
        last_col_index = col_num+level
        # 当前最后一行的下标
        last_row_index = level+row_num
        # 第一行 顺序遍历
        first_row = matrix[level][level:last_col_index]
        res += first_row
        if(row_num == 1):
            return res
        if(row_num == 2):
            last_row = matrix[last_row_index-1][last_col_index-matrix_col_num-1:level-matrix_col_num-1:-1]
            res += last_row
            return res
        # 中间的遍历最后一个元素
        middle_row = [x[level+col_num-1] for x in matrix[level+1:last_row_index-1]]
        res += middle_row
        # 最后一行倒叙遍历
        last_row = matrix[last_row_index-1][last_col_index-matrix_col_num-1:level-matrix_col_num-1:-1]
        res += last_row
        if(col_num == 1):
            return res
        # 左侧 遍历第一个元素
        middle_left_row = [x[level] for x in matrix[last_row_index-1-matrix_row_num-1:level+1-matrix_row_num-1:-1]]
        res += middle_left_row
        return res


s = Solution()
print(s.spiralOrder([[3],[2]]))
