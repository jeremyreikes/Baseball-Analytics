import csv
import sys

def clean(file):
    year = file.split('/')[-1]   # Grab the year from the inputted filename to append to the end of output file
    p1Id = ''
    p2Id = ''
    with open(file, 'r') as f:
        input = csv.reader(f)
        header = input.next()
        firstRow = input.next()     # Grab the first row of information to use in below equivalence checks 
        with open('startersOnly_' + year, 'w') as f2:
            output = csv.writer(f2)
            output.writerow(header)
            output.writerow(firstRow)
            curGame = firstRow[1]
            p1Id = firstRow[14]
            p2set = 0
            for row in input:
                game = row[1]
                pitcherId = row[14]
                if game == curGame:         # If the game of the given row is equivalent to the current game field...
                    if p1Id == pitcherId or p2Id == pitcherId:
                        output.writerow(row)    # Write output if current pitcher matches the above set pitcherID (same pitcher)
                    else:
                        if p2set == 0: # Set other teams pitcher 
                            p2Id = pitcherId
                            output.writerow(row)
                            p2set = 1
                else:   # If new game, reset pitchers
                    curGame = game
                    p1Id = pitcherId
                    p2set = 0
                    p2Id = ''
                    output.writerow(row)


    print "Conversion to starters only complete for " + year

def main(argv):
    '''
    Takes a file from the command line and creates a new file with all relievers removed
    None -> None
    '''
    for arg in sys.argv[1:]:
        arg = str(arg)
        try:
            clean(arg)
        except IOError:
            print "Please input valid filname/path. Erroneous file is " + arg
            continue
        

if __name__ == "__main__":
   main(sys.argv)