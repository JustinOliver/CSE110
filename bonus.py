# Masking Email
email = input("What is your email address?:")
lowerEmail = email.lower()
splitEmail = lowerEmail.split('@')
astrixEmail = (splitEmail[0][0]) + ("******") + (splitEmail[0][-1])
joinedEmail = astrixEmail + "@" + splitEmail[1]
print(joinedEmail)

# Masking Phone Number
number = input("What is your phone number?")
removeChars = ['+','(', ')', ' ', '-']
for char in removeChars:
	number = number.replace(char, '')
localNumber = number[-10:]
localNumberList = list(localNumber)
for i in range(len(localNumberList[:-4])):
	localNumberList[i] = '*'
localNumberList.insert(-7,"-")
localNumberList.insert(-4,"-")
newLocalNumber = "".join(localNumberList)

if len(number) == 13 :
	newLocalNumber = "+***-" + newLocalNumber
elif len(number) == 12:
	newLocalNumber ="+**-" + newLocalNumber
elif len(number) == 11:
	newLocalNumber = "+*-" + newLocalNumber
else:
	pass
print(newLocalNumber)

