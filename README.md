# CSCI345PasswordCracker
Homework 1: A password cracker 

Create File of users & passwords, colon delimited <br>
Import file into program and store them somewhere <br>
encrypt password using library of choice & store that <br>
create regex dictonaries from rules & throw them into encryption fuction <br>
compare to passwords & match <br>
output password to file & terminal<br>

Rule Plans: <br>
(1) A sevenchar word from/usr/share/dict/words (Linux or Mac) which gets the firstletter capitalized and a 1-digit number appended. <br>
search entire library for 7 charcter words, discard anything that isnt 7 characters, the add on the end 0-9 and test it all<br>
(2) A fivedigit password with at least one of the following special charactersin the beginning: *, ~, !, # <br>
for every special character append 0000-9999<br>
(3) A five char word from/usr/share/dict/wordswith the letter 'a' in it which gets replaced with the special character @ and the character ‘l’ is substituted by the number ‘1’. <br>
loop through dictoarny, for every 5 character word switch out all the required characters<br>
(4)Any word that is made with digits up to 7digits length<br>
for loop 0000000-9999999<br>
(5)Any number of chars single word from /usr/share/dict/words (Linux or Mac)<br>
loop through all words
