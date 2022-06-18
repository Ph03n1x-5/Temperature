# Import customized functions
from myCustomFunctions import *


def toFixed(value, digits):
    return "%.*f" % (digits, value)

fileName = ''
outFile = ''

fileName, outFile = createOutputFile()

# ask user to input file name
print("Enter the name of the state you are recording the daily temperature for [i.e. Florida, George, New York]")

# decalre variables
# input statements
state = input()
average = 0
gCount = 0
i = 0

# ask user how many days will they be recording temperature for
print("How many days will you record the outdoor temperature for the state of")
days = checkIntDataType() # call function to check the integer data type and for negative values
wTemp = [0] * (days)
gTemp = [0] * (days)

# gather recorded temps into a list
getData(days, wTemp,state)

# calculate average
average = calculateAverage(wTemp)

# output statements
outFile.write("="*60 + "\n")
outFile.write(("Unsorted Temperature List for the state of " + state).center(60) + "\n")
outFile.write("="*60 + "\n")   
writeList(days,wTemp,outFile)

# write minimum, maximum and average temperatures
outFile.write("="*60 + "\n")
writeStats(wTemp, average, outFile)
outFile.write("="*60 + "\n")

# use the built-in sort function to sort the list from lowest to highest
wTemp.sort()

# output statements
outFile.write("="*60 + "\n")
outFile.write(("Sorted Temperature List for the state of " + state).center(60) + "\n")
outFile.write("="*60 + "\n")
writeList(days,wTemp,outFile)  

# write the stats to an output file
writeStats(wTemp, average, outFile)
outFile.write("="*60 + "\n")

# sort find temps greater than 75
gCount = findTempGreaterthan75(days, wTemp, gTemp, gCount)
outFile.write("="*60 + "\n")

# write temps greater than 75 to an output file
writeTempGreaterthan75(days, gTemp, gCount, outFile)
outFile.write("="*60 + "\n")

# close external file
outFile.close()
# END PROGRAM
