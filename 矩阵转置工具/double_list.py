list01=[[1,1,1],
        [2,2,2],
        [3,3,3]]
def __square_matrix_transpose(list_targe):
    """
        方阵转置
    :param :list_targe 二维列表类型的方阵
    """
    for c in range(1, len(list_targe)):
        for r in range(c, len(list_targe)):
            list_targe[r][c - 1], list_targe[c - 1][r] = list_targe[c - 1][r], list_targe[r][c - 1]
    return list_targe
if  __name__ == "__main__":
    re = __square_matrix_transpose(list01)
    print(re)