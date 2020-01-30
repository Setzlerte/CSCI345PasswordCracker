import hashlib



def openWordList():
	wl = open('/usr/share/dict/words', 'r')
	wordlist = wl.readlines()
	wl.close()
	for i in range(len(wordlist)):
		wordlist[i] = wordlist[i].decode('utf-8')
		wordlist[i] = wordlist[i].replace('\r', '').replace('\n', '')
		#print(len(wordlist[i]))
	return wordlist


def hasher(word):
	return hashlib.sha256(word).hexdigest()
	

def main():
	wordlist = openWordList()
	print("lkajsdfl")
	hashed = hashlib.sha256()
	print(hasher("taco"))
	
	
"""
Input: a digit from 0-9, wordlist from /usr/share/dict/words
Output: a list of seven letter words with the given special number appended at the end
"""
def firstRuleWord(specialNum, wordlist):
	newlist = []
	for i in range(len(wordlist)):
		#print(wordlist[i] + " " + str(len(wordlist[i])))
		if(len(wordlist[i]) == 7):
			newlist.append(wordlist[i] + str(specialNum))
	return newlist
			

def main():
	wordlist = openWordList()
	flist = firstRuleWord(1, wordlist)
	for word in flist:
		print(word)





main()
