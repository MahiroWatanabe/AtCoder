def check_valid(A):
    # 各行について1から9までの数字がちょうど1つずつあるか確認
    for i in range(9):
        if len(set(A[i])) != 9:
            return False

    # 各列について1から9までの数字がちょうど1つずつあるか確認
    for j in range(9):
        col = [A[i][j] for i in range(9)]
        if len(set(col)) != 9:
            return False

    # 3x3のマス目について1から9までの数字がちょうど1つずつあるか確認
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [A[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(square)) != 9:
                return False

    return True


# 9x9のマス目を入力として受け取る
A = [list(map(int, input().split())) for _ in range(9)]

# 条件を満たすかどうかをチェック
result = "Yes" if check_valid(A) else "No"

# 結果を出力
print(result)
