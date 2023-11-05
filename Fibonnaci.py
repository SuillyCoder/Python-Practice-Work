import math
start = int(input("Enter the start number of the Fibonnaci Sequence: "))
end = int(input("Enter the end number of the Fibonnaci Sequence: "))
numIncrement = start
print("Fibbonaci Sequence: ", end = "")
for x in range (end):
        bOne = 1 + math.sqrt(5)
        bTwo = 1 - math.sqrt(5)
        binetOne = (bOne / 2)**numIncrement
        binetTwo = (bTwo / 2)**numIncrement
        wholeBinet = (binetOne - binetTwo) / math.sqrt(5)
        print(int(wholeBinet),end = ", ")
        numIncrement = numIncrement + 1