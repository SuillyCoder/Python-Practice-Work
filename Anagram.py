stringOne = str(input("Input a string: ")).upper()
stringTwo = str(input("Input another string: ")).upper()
startValue = 0 
strOneequal = 0
strTwoequal = len(stringTwo)

for x in range (len(stringOne)):
    if stringOne[startValue] in stringTwo:
        strOneequal = strOneequal + 1
    startValue = startValue + 1

if strOneequal == strTwoequal:
    print("These two strings are anagrams")
else:
    print("These two strings are not anagrams")


