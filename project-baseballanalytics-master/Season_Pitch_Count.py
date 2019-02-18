import time
import csv
from datetime import date, datetime, timedelta



def seasonPitcher2014():
    seasonPitcher('2014_Starter_Order.csv','Season_Pitch_Count_2014.csv')

def seasonPitcher2015():
    seasonPitcher('2015_Starter_Order.csv','Season_Pitch_Count_2015.csv')

def seasonPitcher2016():
    seasonPitcher('2016_Starter_Order.csv','Season_Pitch_Count_2016.csv')

def seasonPitcher2016WS():
    seasonPitcher('2016WS_Starter_Order.csv','Season_Pitch_Count_2016WS.csv')


def getDate(gameID):
    dates = gameID[4:14]
    year = int(dates[:4])
    month = int(dates[5:7])
    day = int(dates[-2:])
    d_time = date(year,month,day)
    return d_time

def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()

def seasonPitcher(infile,outfile):
    with open(infile, 'r') as inputFile, open (outfile, 'w') as pitches:
        inputReader = csv.DictReader(inputFile)
        fieldnames = inputReader.fieldnames + ['weekPitchCount', 'seasonPitchCount']
        pitches_writer = csv.DictWriter(pitches, fieldnames)
        pitches_writer.writeheader()
        pitchCount = 0
        weekPitchCount = 0
        prevPitcherId = None
        prevGameId = None
        lastRestartWeekDate = None
        for row in inputReader:
            if row['pitcherid'] == prevPitcherId:
                pitchCount += 1
                weekPitchCount += 1
                if row['gamestring'] != prevGameId:
                    prevGameId = row['gamestring']
                    day = getDate(row['gamestring'])
                    if (day_Diff(day, lastRestartWeekDate)> 7):
                        lastRestartWeekDate = day
                        weekPitchCount = 1
                        pitchCount += 1
                    else:
                        weekPitchCount +=1
                        pitchCount += 1
            else:
                pitchCount = 1
                weekPitchCount = 1
                prevPitcherId = row['pitcherid']
                prevGameId  = row['gamestring']
                lastRestartWeekDate = getDate(row['gamestring'])
            row['weekPitchCount'] = weekPitchCount
            row['seasonPitchCount'] = pitchCount
            pitches_writer.writerow(row)






def day_Diff(day,prevDay):
    diff = day - prevDay
    return diff.days

if __name__ == "__main__":
    seasonPitcher2016WS()
    seasonPitcher2014()
    seasonPitcher2015()
    seasonPitcher2016()






