import matplotlib.pyplot as plt
import os
import sys
import graphs
import pandas as pd
import csv
from collections import defaultdict
import numpy

['ROB','RISP','Middle_at_Bat','End_Inning','No_Hitter',
 'Shutout','Perfect_Game','Result_last_Pitch','Variance','Score_Against',
 'Score_For','Strikeout_Count','Walk_Count','Hit_Count','Total_Bases','Last_Pitch']

def isolatePitcher(pitcherId):
    # returns every pitch thrown by particular pitcher
    with open('startersOnly_2014.csv', 'r') as f:
        data = csv.reader(f)
        pitcherData = []
        for row in data:
            if row[13] == pitcherId:
                pitcherData.append(row)
        return pitcherData

def isolateByGame(pitcherData):
    # returns a list of lists
    # each entry in the list is a game
    # each list within each game is a pitch
    games = []
    curGame = pitcherData[0][1]
    game = []
    for pitch in pitcherData:
        if pitch[1] == curGame:
            game.append(pitch)
        else:
            curGame = pitch[1]
            games.append(game)
            game = []
    games.append(game)
    return games


def separateByPitchType(games):
    pitches = defaultdict(list)
    for game in games:
        for index, pitch in enumerate(game):
            pitches[pitch[34]].append((pitch[35], index + 1))
    return pitches

def separateByPitchTypeOneGame(games):
    pitches = defaultdict(list)
    for game in games:
        for index, pitch in enumerate(game):
            pitches[pitch[34]].append((pitch[35], index + 1))
        return pitches
    return pitches

def avgBaselinePitchSpeeds(pitches, n):
    speeds = defaultdict(list)
    for pitch in pitches.keys():
        for singlePitch in pitches[pitch]:
            if singlePitch[1] <= n:
                speeds[pitch].append(float(singlePitch[0]))
    avgSpeeds = defaultdict(list)
    for pitch in speeds.keys():
        averageSpeed = sum(speeds[pitch])/len(speeds[pitch])
        stdev = numpy.std(speeds[pitch])
        avgSpeeds[pitch].append(averageSpeed)
        avgSpeeds[pitch].append(stdev)
    return avgSpeeds

pitcherData = isolatePitcher('452657') # corey kluber
gameData = isolateByGame(pitcherData)
pitches = separateByPitchTypeOneGame(gameData)
print pitches
training = avgBaselinePitchSpeeds(pitches, 20)

# pitches = a dictionary with each pitch type as keys, a list of each pitch of that type thrown as the values
