import hashlib

def main():
	wordlist = openWordList()
	flist = firstRuleWord(wordlist)
	secondlist = secondRuleWord()
	thirdlist = thirdRuleWord(wordlist)
	fourthlist = fourthRuleWord()
	
	
	

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
	#allowed = ["*","~","#","!", "0", "1", "2", "3", "4", "5", "6", "7","8","9"]
	allowed = ["*","~","#","!","0"] #added 0 to account for passwords suc as #0001
	newlist = []
	
	for i in range(10000):
		val = str(i)
		if (len(val) == 4):
			for j in range(4): # dont prepend 0s
				newlist.append(allowed[j] + str(i))
			#end for
		elif (len(val) == 3):
			for j in range(4):
				d1 = allowed[j]  #first digit
				for k in range(5): 
					#second digit
					newlist.append(d1 + allowed[k] + val) 
		elif (len(val) == 2):
			for j in range(4):
				d1 = allowed[j] #first digit
				for k in range(5):
					#second digit
					d2 = allowed[k]
					for l in range(5):
						#third digit
						if (k < 4):#dont add special characters after a 0
							newlist.append(d1 + d2 + allowed[l] + val)
						else:
							newlist.append(d1 + d2 + allowed[4] + val)
							break 
						
		
		else:
			for j in range(4):
				d1 = allowed[j] #first digit
				for k in range(5):
					d2 = allowed[k] # second digit
					for l in range(5): #third digit
						if (k < 4): #dont add special characters after a 0
							d3 = allowed[l]
						else:
							d3 = allowed[4]
						for m in range(5):#fourth digit
							if (k < 4 and l < 4):#dont add special characters after a 0
								newlist.append(d1 + d2 + d3 + allowed[m] + val)
							else:
								newlist.append(d1 + d2 + d3 + allowed[4] + val)
								break 
			
			

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

def brute(wordList, hash2Crack):
	"""
	Input:	wordList: the list of words to hash and compare against the hash2Crack
		hash2Crack: hashed value word list is being compared to
	Output: whether the hash was cracked, and if it was, the value of the cracked hash
	"""
	cracked = False
	for i in range(len(wordList)):
		if((hasher(wordlist[i]) == hash2Crack)):
			cracked = True
			break
	if (cracked == True):
		return True, wordList[i]
	else:
		return False

def loginParser(fileName):
	passwordFile = open(fileName, 'r')
	passwords2Crack = []
	usernames = []
	i = 0
	for line in passwordFile:
		userFound = False #tracks if the username has been seperated out
		temp = "" #variable for storing strings
		for char in line: 
			if (str(line[char]) == ":"): #stops at colons, username will be first, then gets the password and stops
				if (found == False):
					userFound = True
					usernames[i] = temp
					temp = ""
				if (found == True):
					break
			else:
				temp += str(line[char])
		passwords2Crack[i] = temp
		i++
			

#end loginParser

main()
