#http://www.ieee.org/membership_services/membership/students/awards/xtremesamples.html

#Cosine simmilarities
# not using any libraries, so ref http://mathforum.org/library/drmath/view/60704.html
'''
Value rank: 40
Simple matching, Jaccard, Tanimoto, and cosine similarities are statistics used for comparing the similarity and diversity of sample sets. They are used in data mining for tasks ranging from classifying diverse chemical compounds, to text processing and searching in large databases.
The sample sets for comparison are represented with vectors of the attributes we want to compare. Given two vectors of attributes, A and B, the cosine similarity, ¦È, can be calculated using the dot product and the magnitudes as:
problem_1
Since the angle, ¦È, is in the range of [0,¦Ð], the resulting similarity will yield the value of ¦Ð as meaning exactly opposite, ¦Ð / 2 meaning independent, 0 meaning exactly the same, with in between values indicating intermediate similarities or dissimilarities.
Your task is to write a program that receives A and B, attribute vectors, and outputs the cosine similarity of those vectors A and B will be entered as parameters in the command line, as square-brackets-delimited, comma-separated lists of integer values, separated by a space. 
The output should be a single line containing the cosine similarity value with four decimals of precision, or the word ERROR if any of the entries are not valid, or the operation cannot be performed
examples
> program [3,2,0,5,0,0,0,2,0,0] [1,0,0,0,0,0,0,1,0,2]
1.2503
> program [6,5,5] [1,1]
Error

> program [,] []
Error

'''

#import math

########################################################

# factorial function
def factorial(x):
	if x == 0:
		return 1
	elif x == 1:
		return 1
	else:
		return x * factorial(x-1)
factorial_str = [factorial(idx) for idx in range(20)]

########################################################

# cos function
def cosfun(x):
	
	iterations = 10;
	x = x * 3.14 / 180
	cnt = 0
	res = 0
	
	for idx in range(iterations):
		if idx % 2 == 0:
			cnt += 1
			sign = (-1) ** (cnt-1)
			res += sign * (x ** idx) / factorial_str[idx]
	
	return res

#print cosfun(60)

########################################################

# sqrt function
def mySqrt(x):
    left = 0.0
    right = 1000.0 # sqrt(C MAX_INT 2147483647)=46340.950001
    while left < right:
        mid = (left + right) / 2
        #print 'mid = ', mid
        if abs(mid ** 2 - x) < 0.0001:
			return mid
        elif x < mid ** 2:
            right = mid - 0.000001
        else:
            left = mid + 0.000001
	#print left, right
#print mySqrt(29)   
           
########################################################

# arctan function
def arctanfun(x):
	iterations = 40;
	#x = x * 3.14 / 180
	cnt = 0
	res = 0
	if abs(x) < 1:
		for idx in range(iterations):
			if idx % 2 == 1:
				cnt += 1
				sign = (-1) ** (cnt-1)
				res += sign * (x ** idx) / idx
		return res
	elif abs(x) == 1:
		res = 3.1415926/4
		return res
	else:
		y = 1.0 / x
		for idx in range(iterations):
			if idx % 2 == 1:
				cnt += 1
				sign = (-1) ** (cnt-1)
				res += sign * (y ** idx) / idx
		return 3.1415926/2 - res

#print arctanfun(1.2), arctanfun(0.3)
#print math.atan(1.2), math.atan(0.3)
#print arctanfun(1), math.atan(1)

########################################################

def arccosfunc(x):
	if 0 < x < 1:
		res = arctanfun(mySqrt(1-x**2) / x)
		return res
	elif -1 < x < 0:
		y = -x
		res = arctanfun(mySqrt(1-y**2) / y)
		return 3.1415926 - res
	elif x == 0:
		return 3.1415926 / 2
	elif x == 1:
		return 0
	elif x == -1:
		return 3.1415926
	
#print math.acos(0.5), arccosfunc(0.5)
#print math.acos(-0.5), arccosfunc(-0.5)

########################################################

def program(str1, str2):
	
	if len(str1) != len(str2):
		print 'Error'
		
	else:
		len_str1 = len(str1)
		len_str2 = len(str2)
		#dot_product = [str1[idx]*str2[idx] for idx in range(len_str1)]
		#abs_str1 = [str1[idx]**2 for idx in range(len_str1)]
		#abs_str2 = [str2[idx]**2 for idx in range(len_str2)]
		#sum_dot_product = sum(dot_product)
	
		res_abs_str1 = 0
		res_abs_str2 = 0
		res_dot_product = []
		for idx in range(len_str1):
			res_abs_str1 += str1[idx]**2
			res_abs_str2 += str2[idx]**2
			res_dot_product.append(str1[idx] * str2[idx])

		res_abs_str1_sqrt = mySqrt(res_abs_str1)
		res_abs_str2_sqrt = mySqrt(res_abs_str2)
	
		numer = sum(res_dot_product)
		denom = res_abs_str1_sqrt * res_abs_str2_sqrt
	
		print arccosfunc(1.0*numer / denom)


str1 = [3,2,4] 
str2 = [1,2,3]
program(str1, str2)

v1,v2 = [3,2,0,5,0,0,0,2,0,0], [1,0,0,0,0,0,0,1,0,2]
program(v1,v2) 

v1,v2 = [6,5,5], [1,1]
program(v1,v2) 


	
	
