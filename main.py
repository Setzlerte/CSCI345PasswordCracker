import hashlib

def main():
	wordlist = openWordList()
	firstlist = firstRuleWord(wordlist)
	secondlist = secondRuleWord()
	thirdlist = thirdRuleWord(wordlist)
	fourthlist = fourthRuleWord()
	fifthlist = fifthRuleWord(wordlist)
	print("lists done")
	usernames, pwd2Crack = loginParser("testPasswords.txt")
	#print(usernames)
	#print(pwd2Crack)
	print("beginning cracking")
	crackedPWDs = crackingMachine(pwd2Crack, firstlist, secondlist, thirdlist, fourthlist, fifthlist)
	print(crackedPWDs)

def openWordList():
	#wl = open('/usr/share/dict/words', 'r')
	wl = open('words.txt', 'r')
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
	
def fifthRuleWord(wordlist):
	return openWordList()

def brute(wordList, hash2Crack):
	"""
	Input:	wordList: the list of words to hash and compare against the hash2Crack
		hash2Crack: hashed value word list is being compared to
	Output: whether the hash was cracked, and if it was, the value of the cracked hash
	"""
	cracked = False
	for i in range(len(wordList)):
		#print(wordList[i])
		if((hasher(wordList[i]) == hash2Crack)):
			cracked = True
			break
	if (cracked == True):
		return True, wordList[i]
	else:
		return False, "nope"

def loginParser(fileName):
	"""
	Input: name of the file to parse for usernames and hashed passwords
	output: a list of usernames and passwords to crack.  Each usernames corresponds to the password in the same position in the other array
	"""
	passwordFile = open(fileName, 'r')
	passwords2Crack = []
	usernames = []
	i = 0
	for line in passwordFile:
		found = False #tracks if the username has been seperated out
		temp = "" #variable for storing strings
		for char in line: 
			if (str(char) == ":"): #stops at colons, username will be first, then gets the password and stops
				if (found == False):
					found = True
					usernames.append(temp)
					temp = ""
				elif ((found == True) and str(char) == ":"):
					break
			else:
				temp += str(char)
		passwords2Crack.append(temp)
		i += 1
	#end for
	return usernames, passwords2Crack
			

#end loginParser

def crackingMachine(passwords2Crack, rule1, rule2, rule3, rule4, rule5):
	pwdCracked = []
	for i in range(len(passwords2Crack)):
		cracked, pwd = brute(rule1,passwords2Crack[i])
		if(cracked == False):	
			#print("not r1")
			cracked, pwd = brute(rule2,passwords2Crack[i])
		if(cracked == False):
			#print("not r2")
			cracked, pwd = brute(rule3,passwords2Crack[i])
		if(cracked == False):	
			#print("not r3")
			cracked, pwd = brute(rule4,passwords2Crack[i])
		if(cracked == False):	
			#print("not r4")
			cracked, pwd = brute(rule5,passwords2Crack[i])
		pwdCracked.append(pwd)
		print(pwd)
	return pwdCracked
		

#end crackingMachine

main()
