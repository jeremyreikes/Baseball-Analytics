import os
import sys
import csv

'''
This file takes the filepath as an argument off of the command line, as well as the first and last N rows of data to gather.
This file also assumes that the data is in sorted or processed based on the following:
    Starters only exist in data with relievers removed
    All pitches for a given pitcher in an appearence follow each other without intermediate pitchers

Please run the program as follows:

python firstLastN.py /dir1/dir2/file.csv N

'''


def grabN(filename, n):
    year = filename.split('/')[-1]
    temp = []

    #For use in indexing into the temporary array 
    currIndex = 1 #Because by the time we use curr index, we should be on the second row, see firstRow below
    n = int(n)
    with open(filename, 'r') as f:
        input = csv.DictReader(f)
        header = input.next() # Skip header
        firstRow = input.next()
        with open('firstLast_'+str(year), 'w') as f2:
            output = csv.writer(f2)
            output.writerow(header.keys())            ## Writes header in output 
            output.writerow(firstRow.values())
            currGame = firstRow['gameString']
            fullTemp = False
            firstN = True
            for row in input:
                #If first N pitches, write to output immediately 
                if currIndex <= n and firstN == True:
                    output.writerow(row.values())
                    if currIndex < n:
                        currIndex += 1
                    else:
                        firstN == False

                #If after first N pitches and not filled buffer, fill buffer from new data
                elif currIndex == n and fullTemp == False:
                    temp.append(row.values())
                    if len(temp) == n:
                        fullTemp = True
                        currIndex = 0

                #If after filled buffer, rotate through the values in buffer, replacing oldest first
                elif fullTemp == True:
                    print currIndex
                    temp[currIndex] = row.values()
                    currIndex += 1 
                    if currIndex == n:
                        currIndex = 0

                #If new new game (assuming cleaned starters only data), output last n rows and restart
                elif row['gameString'] != currGame:
                    writeTemp(output, temp)
                    currGame = row['gameString']
                    temp = []
                    currIndex = 0

            # If you are done looping with a non-full buffer 
            if fullTemp == False:
                writeTemp(output, temp)


def writeTemp(outputWriter, temp):
    for item in temp:
        outputWriter.writerow(item)

def main(argv):
    for arg in argv[1:-1]:
        arg = str(arg)
        grabN(arg, argv[-1])

        print "\nData Processing Complete.\n"




if __name__ == "__main__":
   main(sys.argv)