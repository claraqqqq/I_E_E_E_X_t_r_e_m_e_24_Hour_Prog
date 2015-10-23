# #https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/magic-square

# Telephone keyboard input recognition

'''
Value rank: 60
On a standard telephone, the numbers 1-9 can be used to correspond to a set of letters:
1: space            2: ABC     3: DEF       4: GHI               5: JKL       6: MNO
7: PQRS           8: TUV      9: WXYZ
Using the keypad, you can 'spell' words by entering the digits that correspond to each letter of the word. For example, 'words' is spelled 96737.
For this problem, we are given a dictionary file called with no more than 100,000 words, one per line, sorted in alphabetical order. Each word is comprised of no more than 18 characters, all lowercase letters from the phone keypad. Here is a (very short!) example of a dictionary file we will use in the examples:
Your program should read a string of digits (from 2 to 9, not using 1 as space) from the console and find the words in the dictionary whose spellings contain that series of consecutive digits anywhere within the word.
• If there are no matches, print the string 'No matches'
• If there is one match, print the matching word.
• If there are n>1 matches, print the string 'n matches:' followed by the matching
words, one per line.
NOTE: To make it easier to read the examples below, these are the 'spellings' of the words in words.txt, in digits:
cappuccino: 2277822466
chocolate: 246265283
cinnamon: 24662666
coffee: 263333
latte: 52883
vanilla: 8264554
examples
 contents of words.txt:
cappuccino
chocolate
cinnamon
coffee
latte
vanilla
> program words.txt 22222
No matches
> program words.txt 3333
coffee
> program words.txt 626
2 matches:
chocolate
cinnamon

'''

########################################################

def loadWords(filename):
    inFile = open(filename, 'r', 0)
    res = []
    for line in inFile:
		res.append(line.split('\n')[0])
    return res

#print loadWords('words.txt')

########################################################

def problem2(filename, code):
	dic = {'1':' ', '2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}
	for key in dic.keys():
		dic[key] = dic[key].lower()
		
	words = loadWords('words.txt')
	dic_new = {}

	for word in words:
		dic_new[word] = ''
		for char in word:
			for key in dic.keys():
				if char in dic[key]:
					dic_new[word] += key
	
	cnt = 0
	res = []
	for key in dic_new.keys():
		if code in dic_new[key]:
			cnt += 1
			res.append(key)
	if cnt == 0:
		print 'No matches \n'
	elif cnt == 1:
		print res[0]
	else:
		print cnt, 'matches: \n'
		for word in res:
			print word
	
problem2('words.txt', '22222') 
print '\n'
problem2('words.txt', '3333')
print '\n'
problem2('words.txt', '626')	
	
	
