# Ukuran Papan Catur
n = 8


def isSafe(x, y, board): 
    ''' 
    Fungsi utilitas untuk memeriksa apakah i, j adalah indeks yang valid 
    untuk papan catur berukuran N*N 
    '''
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
        return True
    return False


def printSolution(n, board): 
    ''' 
    Fungsi utilitas untuk mencetak matriks Papan Catur 
    '''
    for i in range(n): 
        for j in range(n): 
            print(board[i][j], end=' ') 
        print() 


def solveKT(n): 
    ''' 
    Fungsi ini menyelesaikan masalah Tur Knight menggunakan 
    Backtracking. Fungsi ini utamanya menggunakan solveKTUtil() 
    untuk menyelesaikan masalah. Fungsi ini mengembalikan False 
    jika tidak ada tur lengkap yang mungkin, sebaliknya mengembalikan 
    True dan mencetak tur. 
    Harap dicatat bahwa mungkin ada lebih dari satu solusi, 
    fungsi ini mencetak salah satu solusi yang memungkinkan. 
    '''

    # Inisialisasi matriks Papan 
    board = [[-1 for i in range(n)]for i in range(n)] 

    # move_x dan move_y menentukan langkah selanjutnya Knight. 
    # move_x adalah untuk nilai x koordinat berikutnya 
    # move_y adalah untuk nilai y koordinat berikutnya 
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 

    # Karena Knight awalnya berada di blok pertama 
    board[0][0] = 0

    # Penghitung langkah untuk posisi Knight 
    pos = 1

    # Memeriksa apakah solusi ada atau tidak 
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)): 
        print("Solusi tidak ada") 
    else: 
        printSolution(n, board) 


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos): 
    ''' 
    Fungsi utilitas rekursif untuk menyelesaikan masalah Tur Knight 
    '''

    if(pos == n**2): 
        return True

    # Mencoba semua langkah selanjutnya dari koordinat x, y saat ini 
    for i in range(8): 
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i] 
        if(isSafe(new_x, new_y, board)): 
            board[new_x][new_y] = pos 
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)): 
                return True

            # Backtracking 
            board[new_x][new_y] = -1
    return False


# Kode Utama 
if __name__ == "__main__": 
    # Panggilan Fungsi 
    solveKT(n)
