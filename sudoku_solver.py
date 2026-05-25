#sodok rodok
def print_board(board):
    """Fungsi untuk menampilkan papan Sudoku ke layar dengan rapi"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Mencari kotak yang masih kosong (direpresentasikan dengan angka 0)"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Mengembalikan posisi (baris, kolom)
    return None

def is_valid(board, num, pos):
    """Mengecek apakah angka yang dimasukkan valid sesuai aturan Sudoku"""
    # Cek Baris
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Cek Kolom
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Cek Kotak 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Fungsi utama algoritma Backtracking untuk menyelesaikan Sudoku"""
    find = find_empty(board)
    if not find:
        return True # Jika tidak ada yang kosong, berarti Sudoku selesai!
    else:
        row, col = find

    # Coba masukkan angka 1 sampai 9
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i # Masukkan angka jika valid

            # Panggil fungsi solve lagi untuk kotak kosong berikutnya
            if solve(board):
                return True

            # BACKTRACKING: Jika di langkah depan mentok, kosongkan lagi kotak ini (jadikan 0)
            board[row][col] = 0

    return False

# ==========================================
# CONTOH PENGGUNAAN
# Angka 0 mewakili kotak yang kosong/belum diisi
# ==========================================
papan_sudoku = [
    [0, 7, 3, 0, 0, 2, 0, 0, 0,],
    [0, 0, 0, 0, 7, 0, 3, 0, 0,],
    [0, 0, 1, 0, 3, 0, 8, 7, 0,],
    [0, 0, 0, 2, 6, 0, 0, 8, 0,],
    [0, 0, 0, 5, 0, 0, 0, 2, 0,],
    [0, 0, 2, 0, 0, 0, 1, 3, 7,],
    [6, 0, 0, 4, 8, 9, 0, 0, 0,],
    [0, 2, 0, 0, 0, 0, 9, 0, 8,],
    [8, 0, 0, 0, 0, 0, 0, 0, 1,]
]

print("PAPAN SUDOKU SEBELUM DIKERJAKAN:")
print_board(papan_sudoku)
print("\nSedang memecahkan...\n")

solve(papan_sudoku)

print("PAPAN SUDOKU SETELAH DISELESAIKAN:")
print_board(papan_sudoku)
          
