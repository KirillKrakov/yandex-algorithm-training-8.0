def main():
    import sys
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Если поле слишком маленькое
    if n < 5 and m < 5:
        print("No")
        return
    
    field = [sys.stdin.readline().strip() for _ in range(n)]
    
    # Проверяем строки
    for i in range(n):
        count_x = count_o = 0
        for j in range(m):
            if field[i][j] == 'X':
                count_x += 1
                if count_x >= 5:
                    print("Yes")
                    return
            else:
                count_x = 0
                
            if field[i][j] == 'O':
                count_o += 1
                if count_o >= 5:
                    print("Yes")
                    return
            else:
                count_o = 0
    
    # Проверяем столбцы
    for j in range(m):
        count_x = count_o = 0
        for i in range(n):
            if field[i][j] == 'X':
                count_x += 1
                if count_x >= 5:
                    print("Yes")
                    return
            else:
                count_x = 0
                
            if field[i][j] == 'O':
                count_o += 1
                if count_o >= 5:
                    print("Yes")
                    return
            else:
                count_o = 0
    
    # Проверяем только возможные диагонали
    # Вниз-вправо
    for i in range(n - 4):
        for j in range(m - 4):
            # Проверяем X
            count_x = 0
            for k in range(5):
                if field[i + k][j + k] == 'X':
                    count_x += 1
            if count_x >= 5:
                print("Yes")
                return
            
            # Проверяем O
            count_o = 0
            for k in range(5):
                if field[i + k][j + k] == 'O':
                    count_o += 1
            if count_o >= 5:
                print("Yes")
                return
    
    # Вниз-влево
    for i in range(n - 4):
        for j in range(4, m):
            # Проверяем X
            count_x = 0
            for k in range(5):
                if field[i + k][j - k] == 'X':
                    count_x += 1
            if count_x >= 5:
                print("Yes")
                return
            
            # Проверяем O
            count_o = 0
            for k in range(5):
                if field[i + k][j - k] == 'O':
                    count_o += 1
            if count_o >= 5:
                print("Yes")
                return
    
    print("No")

if __name__ == '__main__':
    main()
