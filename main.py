import hashlib

def main():
	"""
	wordlist = openWordList()
	flist = firstRuleWord(wordlist)
	thirdlist = thirdRuleWord(wordlist)
	fourthlist = fourthRuleWord()
	for word in fourthlist:
		print(word)
	"""
	secondlist = secondRuleWord()

def openWordList():
	wl = open('/usr/share/dict/words', 'r')
	wordlist = wl.readlines()
	wl.close()
	for i in range(len(wordlist)):
		wordlist[i] = wordlist[i].decode('utf-8')
		wordlist[i] = wordlist[i].replace('\r', '').replace('\n', '')
		wordlist[i] = wordlist[i].title()
		#print(len(wordlist[i]))
	return wordlist

"""
input: a string(word) to be hashed
output: the sha256 hexidecimal hash of word  
"""
def hasher(word):
	return hashlib.sha256(word).hexdigest()
	
	

"""
Input: a digit from 0-9, wordlist from /usr/share/dict/words
Output: a list of seven letter words with the given special number appended at the end
"""
def firstRuleWord(wordlist):
	newlist = []
	for j in range(10):
		for i in range(len(wordlist)):
			#print(wordlist[i] + " " + str(len(wordlist[i])))
			if(len(wordlist[i]) == 7):
				newlist.append(wordlist[i] + str(j))
	return newlist
			

"""
output: list of a 5 digit string with special characters beginning in the front of the string
"""
def secondRuleWord():
	allowed = ["*","~","#","!", "0", "1", "2", "3", "4", "5", "6", "7","8","9"]
	newlist = []
	for special in range(4):
		#first digit 
		for d2 in range(len(allowed)):
			#second digit
			for d3 in range(len(allowed)):
				#third digit
				for d4 in range(len(allowed)):
					#fourth digit
					for d5 in range(len(allowed)):
						#last digit
						newlist.append(allowed[special] + allowed[d2] + allowed[d3] + allowed[d4] + allowed[d5])
						
	# end special loop
	print(newlist)	
	return newlist
	

def thirdRuleWord(wordlist):
	newlist = []
	for word in wordlist:
		if(len(word) == 5 and 'a' in word and 'l' in word):
			word = word.replace('a', '@').replace('l', '1')
			newlist.append(word)
	return newlist

def fourthRuleWord():
	newlist = []
	for i in range(10000000):
		newlist.append(str(i))
	return newlist
main()
