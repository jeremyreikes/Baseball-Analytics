import matplotlib.pyplot as plt
import os
import sys
import csv
from collections import defaultdict
import numpy
import tree
from tree import *

new_fields = ['ROB','RISP','middle_at_bat','end_inning','no_hitter',
              'shutout','perfect_game','variance','score_against',
              'score_for','strikeout_count','walk_count','hit_count','total_bases', 'pitch_number', 'last_pitch_game', 
              'B_score_against','B_score_for','B_strikeout_count','B_walk_count','B_hit_count','B_total_bases', 'B_pitch_number']

buckets = ['B_score_against','B_score_for','B_strikeout_count','B_walk_count','B_hit_count','B_total_bases', 'B_pitch_number']

class Game:
    ''' 
    Class that represents an individual game for a given pitcher. Keeps track of and accumulates data to represent an appearence in a game.
    '''

    def __init__(self):
        self.ROB = False 
        self.RISP = False 
        self.middle_at_bat = True 
        self.end_inning = False  
        self.no_hitter = True  
        self.shutout = True  
        self.perfect_game = True 
        self.variance = 0  
        self.score_against = 0
        self.score_for = 0
        self.strikeout_count = 0  
        self.walk_count = 0 
        self.hit_count = 0  
        self.total_bases = 0  
        self.pitch_number = 0 
        self.last_pitch_game = False

    def getFields(self):
        '''
        Returns all fields in the form of a list.
        (self) -> list
        '''
        return [self.ROB, self.RISP, self.middle_at_bat, self.end_inning, self.no_hitter,
                self.shutout, self.perfect_game, self.variance, self.score_against,
                self.score_for, self.strikeout_count, self.walk_count, self.hit_count, 
                self.total_bases,  self.pitch_number, self.last_pitch_game]

    def handlePA(self, paResult):
        '''
        Takes in the paResult for a given pitch and updates instance variables based on the result of the pitch.
        (self, str) -> None
        '''
        if paResult == 'K':
            self.strikeout_count += 1
        if paResult == 'BB' or paResult == 'HBP':
            self.walk_count += 1
            self.total_bases += 1
            self.perfect_game = False
        if paResult == 'S':
            self.hit_count += 1
            self.total_bases += 1
            self.no_hitter = False
            self.perfect_game = False
        if paResult == 'D':
            self.hit_count += 1
            self.total_bases += 2
            self.no_hitter = False
            self.perfect_game = False
        if paResult == 'T':
            self.hit_count += 1
            self.total_bases += 3
            self.no_hitter = False
            self.perfect_game = False
        if paResult == 'HR':
            self.hit_count += 1
            self.total_bases += 4
            self.no_hitter = False
            self.perfect_game = False
        if paResult == 'IBB' or paResult == 'ROE' or paResult == 'CI' or paResult == 'FI':
            self.perfect_game = False

        #handle middle_at_bat
        if paResult == '':
            self.middle_at_bat = True
        else:
            self.middle_at_bat = False
# End class

# Takes a file that has been previously cleaned of all it's relievers, and adds all the new fields

def isolateByGame(pitcherData):
    # returns a list of lists
    # each entry in the list is a game
    # each list within each game is a pitch
    '''
    Returns a list of lists with each list entry in the outter list representing a game and each list within a game representing a pitch.
    (Dict) -> [[list]]
    '''
    games = []
    currGame = pitcherData[0][1]
    game = []
    for pitch in pitcherData:
        if pitch[1] == currGame:
            game.append(pitch)
        else:
            currGame = pitch[1]
            games.append(game)
            game = []
            game.append(pitch)
    games.append(game)
    return games

def handlePitcher(output, pitcherData, inningSplit):
    '''
    Handles writing of fields for individual pitchers, takes in the output file
    to write to and the pitcherData (a list of all pitches by that pitcher) as 
    well as an inning split as a point from which to start writing data.
    (file, [list], int) -> None
    '''
    games = isolateByGame(pitcherData)
    for game in games:
        currGame = Game()
        for index, pitch in enumerate(game):
            if int(pitch[8]) < int(inningSplit):
                continue
            #get pitch results
            paResult = pitch[52]
            runsOnPitch = pitch[53]
            side = pitch[9]
            homeRuns = pitch[31]
            awayRuns = pitch[32]
            manOnFirstAfter = pitch[28]
            manOnSecondAfter = pitch[29]
            manOnThirdAfter = pitch[30]
            inning = pitch[8]
            #handle ROB, RISP
            if manOnFirstAfter == 'true' or manOnSecondAfter == 'true' or manOnThirdAfter == 'true':
                currGame.ROB = True
            else:
                currGame.ROB = False
            if manOnSecondAfter == 'true' or manOnThirdAfter == 'true':
                currGame.RISP = True
            else:
                currGame.RISP = False

            #handle score_against, score_for
            if runsOnPitch == '': # if didn't score on pitch
                if side == 'T':
                    currGame.score_against = homeRuns
                else:
                    currGame.score_against = awayRuns
            else:
                if side == 'T':
                    currGame.score_against = str(int(homeRuns) + int(runsOnPitch))
                else:
                    currGame.score_against = str(int(awayRuns) + int(runsOnPitch))
            if side == 'T':
                currGame.score_for = awayRuns
            else:
                currGame.score_for = homeRuns
            #done

            #handle total bases, strikeout_count, walk_count, hit_count, no_hitter, perfect_game
            currGame.handlePA(paResult)

            #handle pitch_number
            currGame.pitch_number += 1

            #handle shutout
            if int(currGame.score_against) > 0:
                currGame.shutout = False

            #handle last_pitch_game
            if pitch == game[-1]:
                currGame.last_pitch_game = True
            else:
                currGame.last_pitch_game = False

            # handle end_inning
            if currGame.last_pitch_game == False:
                if inning != game[index + 1][8]:
                    currGame.end_inning = True
                else:
                    currGame.end_inning = False
            else:
                currGame.end_inning = True

            fieldsToAdd = currGame.getFields()
            bucketsToAdd = bucketize(fieldsToAdd)
            pitch[52] = paBuckets(paResult)
            output.writerow(pitch + fieldsToAdd + bucketsToAdd)

        currGame = None

def writePitchers(file, flag, inningSplit):
    '''
    Takes in a file and a flag from the command line (file as input,
    flag as pitcher ID or all if you want to write output for all pitchers).
    (str, str) -> None
    '''
    with open('new_fields_' + flag + '_'+ file, 'w') as f:
        output = csv.writer(f)
        try:    
            pitcherDict, header = parseFile(file)
        except IOError:
            print "Please input valid filename/path."
            f.close()
            os.remove(f.name)
            return 
        header += new_fields
        output.writerow(header)
        if flag == 'all':
            for pitcherId in pitcherDict.keys():
                pitcherData = pitcherDict[pitcherId]
                handlePitcher(output, pitcherData, inningSplit)
            print "Pitcher(s) written successfully"
        else:
            try:
                handlePitcher(output, pitcherDict[flag], inningSplit)
                print "Pitcher(s) written successfully"
            except KeyError:
                f.close()
                os.remove(f.name)
                print "\nMust input valid pitcher ID or 'all' as second argument. \n"

def paBuckets(paResult):
    '''
    This function takes in the paResult from the pitch and reduces it down to fewer buckets.
    (str) -> str
    '''
    if paResult == '':
        return 'DURING'
    elif paResult == "IP_OUT" or paResult == "DP" or paResult == "TP" or paResult == "FC":
        return 'OUT'
    elif paResult == 'S':
        return 'SINGLE'
    elif paResult == 'D':
        return 'DOUBLE'
    elif paResult == 'T':
        return 'TRIPLE'
    elif paResult == 'HR':
        return 'HOMERUN'
    elif paResult == 'BB' or paResult == 'HBP':
        return 'WALK'
    elif paResult == 'K':
        return 'STRIKEOUT'
    else:
        return 'MISC'

def bucketize(fields):
    '''
    This function takes in the fields from the currGame class and places 
    them in buckets as strings that represent ranges. This is so that the 
    decision tree will have a more wieldy feature to split on.

    (list) -> list
    '''
    output = []
    score_against = fields[8]
    if int(score_against) < 2: 
        output.append("0-1")
    elif int(score_against) < 5: 
        output.append("2-4")
    else:
        output.append("5+"
)
    score_for = fields[9]
    if int(score_for) < 2: 
        output.append("0-1")
    elif int(score_for) < 5: 
        output.append("2-4")
    else:
        output.append("5+")

    strikeout_count = fields[10]
    if int(strikeout_count) < 4:
        output.append("0-3")
    elif int(strikeout_count) < 7:
        output.append("4-6")
    else:
        output.append("7+")

    walk_count = fields[11]
    if int(walk_count) < 2:
        output.append("0-1")
    elif int(walk_count) < 5:
        output.append("2-4")
    else:
        output.append("5+")

    hit_count = fields[12]
    if int(hit_count) < 4:
        output.append("0-3")
    elif int(hit_count) < 7:
        output.append("4-6")
    else:
        output.append("7+")

    total_bases = fields[13]
    if int(total_bases) < 8:
        output.append("0-7")
    elif int(total_bases) < 14:
        output.append("8-13")
    else:
        output.append("14+")

    pitch_count = fields[14]
    if int(pitch_count) < 61:
        output.append("1-60")
    elif int(pitch_count) < 81:
        output.append("61-80") 
    elif int(pitch_count) < 91:
        output.append("81-90")
    elif int(pitch_count) < 96:
        output.append("91-95")
    elif int(pitch_count) < 101:
        output.append("96-100")
    elif int(pitch_count) < 106:
        output.append("101-105")
    elif int(pitch_count) < 111:
        output.append("106-110") 
    else:
        output.append("111+")

    return output

def parseFile(filename):
    '''
    Takes in the input file and creates a dictionary with each key representing
    a pitcher ID and the values of each key being each pitch thrown by that pitcher.
    It also returns the header of the input file to write to the output file. 
    (file) -> dict, lisr
    ''' 
    pitcherData = {}
    with open(filename, 'r') as f:
        input = csv.reader(f)
        header = input.next()
        for pitch in input:
            if pitch[13] in pitcherData.keys():
                pitcherData[pitch[13]].append(pitch)
            else:
                pitcherData[pitch[13]] = [pitch]
    return pitcherData, header

def main(argv):
    try:
        file = str(argv[1])
        flag = str(argv[2])
        inningSplit = str(argv[3]) # Inning from which to start writing data, with one capturing all innings and nine capturing just the ninth inning etc. 
    except IndexError:
        print "Please input the correct arguments: filename, flag, inning"
        return
    try: 
        if int(inningSplit) <= 9:
            writePitchers(file, flag, inningSplit)
        else:
            print "Please input valid inning number (1-9)."
    except ValueError:
        print "Please input valid inning number (1-9)."
    

if __name__ == "__main__":
   main(sys.argv)





