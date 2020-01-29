import hashlib

rule1 = '([A-Z][a-z]{6}[0-9])'
rule2 = ''
rule3 = ''
rule4 = ''
rule5 = ''

def openWordList():
	wl = open('/usr/share/dict/words', 'r')
	wordlist = wl.readlines()
	wl.close()
	return wordlist

"""
Input: a digit from 0-9, wordlist from /usr/share/dict/words
Output: a list of seven letter words with the given special number appended at the end
"""
def firstRuleWord(specialNum, wordlist):
	

def main():
	wordlist = openWordList()
	print("lkajsdfl")





main()
