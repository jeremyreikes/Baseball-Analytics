import time
import csv
from datetime import date, datetime



def gamePitcher2014():
    gamePitcher('startersOnly_2014.csv','starters_Pitch_Count_2014.csv')

def gamePitcher2015():
    gamePitcher('startersOnly_2015.csv','starters_Pitch_Count_2015.csv')

def gamePitcher2016():
    gamePitcher('startersOnly_2016.csv','starters_Pitch_Count_2016.csv')

def gamePitcher2016WS():
    gamePitcher('startersOnly_2016-WS.csv','starters_Pitch_Count_2016-WS.csv')



def gamePitcher(infile,outfile):
    with open(infile, 'r') as inputFile, open (outfile, 'w') as pitches:
        inputReader = csv.DictReader(inputFile)
        fieldnames = inputReader.fieldnames + ['gamePitchCount']
        pitches_writer = csv.DictWriter(pitches, fieldnames)
        pitches_writer.writeheader()
        prevGameString = None
        gamePitchCount = 0
        otherPitcherCount = 0
        prevPitcherId = None
        for row in inputReader:
            #if its the same game
            if (row['gameString'] == prevGameString):
                #if its the same pitcher increment pitch count and write
                if (row['pitcherId'] == prevPitcherId):
                    gamePitchCount = gamePitchCount + 1
                    row['gamePitchCount'] = gamePitchCount
                #if its the other pitcher, switch variables, increment pitch count, and write
                else:
                    tmpPitchCount = otherPitcherCount
                    otherPitcherCount = gamePitchCount
                    gamePitchCount = tmpPitchCount
                    prevPitcherId = row['pitcherId']
                    gamePitchCount = gamePitchCount + 1
                    row['gamePitchCount'] = gamePitchCount
            #first pitch of new game, reset variables, write pitch count = 1
            else:
                prevGameString = row['gameString']
                gamePitchCount = 1
                otherPitcherCount = 0
                prevPitcherId = row['pitcherId']
                row['gamePitchCount'] = gamePitchCount
            pitches_writer.writerow(row)

def getDate(gameID):
    dates = gameID[4:14]
    year = int(dates[:4])
    month = int(dates[5:7])
    day = int(dates[-2:])
    d_time = date(year,month,day)
    return d_time

if __name__ == "__main__":
    #getDate('gid_2014_03_22_lanmlb_arimlb_1')
    '''
    gamePitcher2014()
    print("Created for 2014")
    gamePitcher2015()
    print("Created for 2015")
    gamePitcher2016()
    print("Created for 2016")
    '''
    gamePitcher2016WS()
    print("Created for 2016WS")






