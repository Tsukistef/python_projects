ragged_list = [ [ 1, 2, 3 ] ,
[ 4, 5 ],
[ 6 ],
[ 7, 8, 9, 10 ] ]

rows = len(ragged_list)
for row in range(len(ragged_list)):
    cols = len(ragged_list[row])
    print('Row ', row, 'has', cols, 'columns ', end="")
    for col in range(cols):
        print(ragged_list[row][col], " ", end="")
    print()
