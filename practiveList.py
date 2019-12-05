def practiveList(list1):
    str = ""
    for i in range(len(list1)):
        if i <> 0:
            str = str + "\n"
        for j in range(len(list1[i])):
            str = str + list1[i][j] + ","
    print str    
def main():
    list1 = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    practiveList(list1)
    
main()