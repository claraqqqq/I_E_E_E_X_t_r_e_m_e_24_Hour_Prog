# Sum it up

'''
Problem Statement

Minka is very smart kid who recently started learning computer programming. 
His coach gave him a cyclic array A having N numbers, and he has to perform Q operations on this array. 
In each operation the coach would provide him with a number X. After each operation, every element of the cyclic array would be replaced by the sum of itself and the element lying X positions behind it in the cyclic array. All these replacements take place simultaneously. 
For example, if the cyclic array was [a, b, c, d], then after the operation with X = 1, the new array would be [a+d, b+a, c+b, d+c]. 
He needs to output the sum of the elements of the final array modulus 10^9+7. 
He made a program for it but it's not very efficient. You know he is a beginner, so he wants you to make an efficient program for this task because he doesn't want to disappoint his coach.

Input

The first line of each test file contains a integer N (1 <= N <= 100000). 
The next line contains N space separated integers which represent the elements of the cyclic array ( 1 <= Ai <= 10^9 ). 
The third line contains a integer Q (0 <= Q <= 1000000) representing the number of operations that will be applied to the array. 
Finally, Q lines follow, each one containing an integer X (0 <= X < N).

Output

Your program should output to the standard output stream the sum of the elements of the final array modulus 10^9+7. 
Note: There is a newline character at the end of the last line of the output.

Sample Input 1

5   
1 2 3 4 5   
2   
1   
0   
Sample Output 1

60   
Explanation of Sample Input 1

After the 1st operation (X = 1), the array would be [1+5, 2+1, 3+2, 4+3, 5+4] = 
[6, 3, 5, 7, 9]
After 2nd operation (X = 0), the array would be [6+6, 3+3, 5+5, 7+7, 9+9] = 
[12, 6, 10, 14, 18]
Thus the correct answer would equal to = (12+6+10+14+18) % (10^9+7) = 60
Sample Input 2

5   
1 2 3 4 5   
0   
Sample Output 2

15   
'''

N = int(raw_input())
tmp = raw_input().split()
arr = [int(tmp[idx]) for idx in range(N)]
NumOper = int(raw_input())
integers = []
for idx in range(NumOper):
	integers.append(int(raw_input()))

def shift(lst, num):
	length = len(lst)
	return lst[length-num:] + lst[:length-num]


def SumItUp():
	
	#res = [[] for idx in range(NumOper+1)]
	#res[0] = arr	
	
	#if NumOper == 0:
	#	return sum(arr)
		
	#for idx in range(NumOper):
	
	#   method 1
	#	shift_arr = shift(res[idx], integers[idx])
	#	res[idx+1]  = [sum(x) for x in zip(shift_arr, res[idx])]
	#print res
	#   method 2
		#for idy in range(N):			
			#res[idx+1].append(res[idx][idy] + res[idx][idy-integers[idx]])
	
	#res = arr
	#for idx in range(NumOper):
	#   method 3
		#shift_arr = shift(res, integers[idx])
		#res = [sum(x) for x in zip(shift_arr, res)]
	#   method 4
	#	tmp = res[:]
	#	for idy in range(N):		
	#		res[idy] = tmp[idy] + tmp[idy-integers[idx]]
	
	res = sum(arr) * (2 ** NumOper)
	return res % (10**9+7) 

print SumItUp()
