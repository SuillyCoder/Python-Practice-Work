emptyList = []
while True:
    userInput = str(input("Input something: "))
    if userInput == "STOP" or userInput == "Stop" or userInput == "stop":
        break
    emptyList.append(userInput)
    
for x in range (2):
    print("")

print("Default List: ",end="")
print(emptyList)
print("")

reversedList = emptyList[::-1]
print("Reversed List: ",end="")
print(reversedList)