def main():
    import sys
    
    n, m = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    
    # Предподсчёт
    base_row = [0] * n
    q_row = [0] * n
    base_col = [0] * m
    q_col = [0] * m
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '+':
                base_row[i] += 1
                base_col[j] += 1
            elif grid[i][j] == '-':
                base_row[i] -= 1
                base_col[j] -= 1
            else:  # '?'
                q_row[i] += 1
                q_col[j] += 1
    
    # Вычисляем диапазоны
    row_min = [base_row[i] - q_row[i] for i in range(n)]
    row_max = [base_row[i] + q_row[i] for i in range(n)]
    col_min = [base_col[j] - q_col[j] for j in range(m)]
    col_max = [base_col[j] + q_col[j] for j in range(m)]
    
    # Пробуем все кандидаты на максимальную строку
    answer = -10**9
    
    for i in range(n):
        
        # Для строки i ставим все ? в + чтобы максимизировать её
        current_max_row = row_max[i]
        
        # Теперь для каждого столбца j: можем ли мы сделать его сумму достаточно малой?
        # При этом учитываем конфликт в ячейке (i,j)
        
        for j in range(m):
            if grid[i][j] == '?':

                
                # Вариант 1: в (i,j) ставим '-'
                min_col1 = base_col[j] - 1 - (q_col[j] - 1)  # все остальные ? в столбце j ставим -
                diff1 = current_max_row - 2 - min_col1  # в строке i стало current_max_row - 2
                
                # Вариант 2: в (i,j) ставим '+'
                min_col2 = base_col[j] + 1 - (q_col[j] - 1)  # все остальные ? в столбце j ставим -
                diff2 = current_max_row - min_col2
                
                current_diff = max(diff1, diff2)
            else:
                # Нет конфликта - можем независимо оптимизировать
                current_diff = current_max_row - col_min[j]
            
            answer = max(answer, current_diff)
    
    print(answer)

if __name__ == '__main__':
    main()
