#Magic Square

'''
Problem Statement

Magic Square

Johnny designed a magic square (square of numbers with the same sum for all rows, columns and diagonals i.e. both the main diagonal - meaning the diagonal that leads from the top-left corner towards bottom-right corner - and the antidiagonal - meaning the diagonal that leads from top-right corner towards bottom-left corner). Write a program to test it.

Task 
Write a program that will check if the given square is magic (i.e. has the same sum for all rows, columns and diagonals).

Input 
First line: N , the size of the square (1 <= N <= 600). 
Next N lines: The square, N space separated integers pre line, representing the entries per each row of the square.

Output 
First line: M , the number of lines that do not sum up to the sum of the main diagonal (i.e. the one that contains the first element of the square). If the Square is magic, the program should output 0. 
Next M lines: A sorted (in incremental order ) list of the lines that do not sum up to the sum of the main diagonal. The rows are numbered 1,2,…,N; the columns are numbered -1,-2,…,-N; and the antidiagonal is numbered zero.

Note: There is a newline character at the end of the last line of the output. 
Sample Input 1 
3 
8 1 6 
3 5 7 
4 9 2

Sample Output 1 
0

Sample Input 2 
4 
16 3 2 13 
5 10 11 8 
6 9 7 12 
4 15 14 1

Sample Output 2 
3 
-2 
-1 
0

Explanation of Sample Output 2 
The input square looks as follows: IMAGE 1

The square has 4 rows (labeled from 1 to 4 in orange) and 4 columns (labeled from -1 to -4 in green) as depicted in the image above. The main diagonal and antidiagonal of the square are highlighted in red and blue respectively.

The main diagonal has sum = 16 + 10 + 7 +1 = 34. 
The antidiagonal has sum = 13 + 11 + 9 + 4 = 37. This is different to the sum of the main diagonal so value 0 corresponding to the antidiagonal should be reported. 
Row 1 has sum = 16 + 3 + 2 + 13 = 34. 
Row 2 has sum = 5 + 10 + 11 + 8 = 34. 
Row 3 has sum = 6 + 9 + 7 + 12 = 34. 
Row 4 has sum = 4 + 15 + 14 + 1 = 34. 
Column -1 has sum = 16 + 5 + 6 + 4 = 31. This is different to the sum of the main diagonal so value -1 should be reported. 
Column -2 has sum = 3 + 10 + 9 + 15 = 37. This is different to the sum of the main diagonal so value -2 should be reported. 
Column -3 has sum = 2 + 11 + 7 + 14 = 34. 
Column -4 has sum = 13 + 8 + 12 + 1 = 34. 
Based on the above, there are 3 lines that do not sum up to the sum of the elements of the main diagonal. Since they should be sorted in incremental order, the output should be: 
3 
-2 
-1 
0
'''

'''
input_list = []

while True:
    input_str = raw_input(">")
    if input_str == ".":
        break
    else:
        input_list.append(input_str)
        print type(input_str)

print input_list
'''

###############################################################
def MagicSquare(stdin):
	N = stdin[0][0]

	mtx = stdin[1:len(stdin)]

	res = []
	main_diag = 0
	anti_diag = 0
	row_rcrd = [0 for idx in range(N)]
	col_rcrd = [0 for idx in range(N)]	
	
	
	for idx in range(N):
		main_diag += mtx[idx][idx]
		anti_diag += mtx[idx][N-1-idx]
		row_rcrd[idx] = sum(mtx[idx])
		col_rcrd[idx] = sum([mtx[idy][idx] for idy in range(N)])
		 
	if main_diag != anti_diag:
		res.append(0)
		
	for idx in range(N):
		if row_rcrd[idx] != main_diag:
			res.append(idx+1)
		if col_rcrd[idx] != main_diag:
			res.append(-(idx+1))
	
	if len(res) == 0:
		print 0
	else:	
		print len(res)
		res.sort()
		for num in res:
			print num 


N = int(raw_input())
stdin = [[N]]
for idx in range(N):
	tmp = raw_input().split()
	stdin.append([int(tmp[idx]) for idx in range(N)])


MagicSquare(stdin)

'''	
stdin = [[3],[8, 1, 6],[3, 5, 7],[4, 9, 2]]	
MagicSquare(stdin)

stdin = [[4], [16, 3, 2, 13], [5, 10, 11, 8], [6, 9, 7, 12], [4, 15, 14, 1]]
MagicSquare(stdin)	
'''



