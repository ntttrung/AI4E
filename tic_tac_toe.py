A = [[0,0,0],[0,0,0],[0,0,0]]

def check_position(x,y,A):
    if A[x][y] == 0:
        return 1
    return 0


def check_win(x,y,A):
    if x == y:
        if (A[0][0] == A[1][1] == A[2][2] !=0) or (A[0][2] == A[1][1] == A[2][0]!= 0):
            return 1
    else:
        if (A[x][0] == A[x][1] == A[x][2] != 0) or (A[0][y] == A[1][y] == A[2][y] != 0):
            return 1
    return 0

count = 0
dk_win = 0
dk_run = 0
while count != 9 and dk_win == 0:
    while dk_run == 0:
        print("Team A")
        x = int(input('x: '))
        y = int(input('y: '))
        if check_position(x,y,A) == 1:
            A[x][y] = 1
            count += 1
            dk_win = check_win(x,y,A)
            if dk_win == 1:
                print("A win")
            dk_run = 1
    if count == 9:
        break
    if dk_win == 0:
        while dk_run == 1:
            print("Team B")
            x = int(input('x: '))
            y = int(input('y: '))
            if check_position(x,y,A) == 1:
                A[x][y] = -1
                count += 1
                dk_win = check_win(x,y,A)
                if dk_win == 1:
                    print("B win")
                dk_run = 0
if count == 9:
    print("Hoa")





