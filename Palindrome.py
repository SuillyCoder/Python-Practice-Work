input = str(input("Input something. Anything: ")).upper()
reversedInput = input[::-1]
if input == reversedInput:
    print("This is a palindrome string")
else: 
    print("This isn't a palindrome string")