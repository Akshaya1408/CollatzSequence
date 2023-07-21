col = int(input())
if col==1:
    print(col//2)

while col > 1:
    if col % 2 == 0:
        col = col // 2
        print(col, end = " ")
    else:
        col = (3*col) + 1
        print(col, end = " ")

    