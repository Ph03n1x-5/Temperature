# Import customized functions
from myCustomFunctions import *


def toFixed(value, digits):
    return "%.*f" % (digits, value)

# initialize variables
fileName = ''
outFile = ''

fileName,outFile = createOutputFile() # call the function to create the external output file
print("Enter the name of the state you are recording the daily temperature for [i.e. Florida, George, New York]")

# decalre variables
# input statements
state = input()
i = 0
print("How many days will you record the outdoor temperature for the state of")
days = checkIntDataType() # call function to check the integer data type and for negative values
wTemp = [0] * (days)

# first while loop
while i < days:
    print("What is the outdoor temperature in " + state + " on day # " + str(i + 1))
    wTemp[i] = checkfloatdata()# call function to check float data type and for negative values
    i = i + 1

# output statements
outFile.write("="*60 + "\n")
outFile.write(("Unsorted Temperature List for the state of " + state).center(60) + "\n")
outFile.write("="*60 + "\n")

# declare more variables
i = 0
total = 0

# second while loop
while i < days:
    outFile.write(("wTemp[" + str(i + 1) + "] = " + format(wTemp[i], "6.2f") + "°").center(60) + "\n")
    total = total + wTemp[i]
    i = i + 1
    # end while loop    

# calculate average and round 2 decimal places
average = total / days

# last output statements
outFile.write("="*60 + "\n")
# Write minimum, maximum and average temperatures
outFile.write(("The minimum Temperature = " + format(min(wTemp), "6.2f") + "°").center(60) + "\n")
outFile.write(("The maximum Temperature = " + format(max(wTemp), "6.2f") + "°").center(60) + "\n")
outFile.write(("THE AVERAGE DAILY TEMPERATURE = " + format(average, "6.2f") + "°").center(60) + "\n")
outFile.write("="*60 + "\n")
outFile.write("="*60 + "\n")

# use the built-in sort function to sort the list from lowest to highest
wTemp.sort()

# write the sorted list
# output statements
outFile.write("="*60 + "\n")
outFile.write(("Sorted Temperature List for the state of " + state).center(60) + "\n")
outFile.write("="*60 + "\n")

# declare more variables
i = 0
total = 0

# second while loop
while i < days:
    outFile.write(("wTemp[" + str(i + 1) + "] = " + format(wTemp[i], "6.2f") + "°").center(60) + "\n")
    total = total + wTemp[i]
    i = i + 1
    # end while loop    

# last output statements
outFile.write("="*60 + "\n")
# Write minimum, maximum and average temperatures
outFile.write(("The minimum Temperature = " + format(min(wTemp), "6.2f") + "°").center(60) + "\n")
outFile.write(("The maximum Temperature = " + format(max(wTemp), "6.2f") + "°").center(60) + "\n")
outFile.write(("THE AVERAGE DAILY TEMPERATURE = " + format(average, "6.2f") + "°").center(60) + "\n")
outFile.write("="*60 + "\n")
outFile.write("="*60 + "\n")

# close external file
outFile.close()
# END PROGRAM
