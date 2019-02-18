import math
import collections
from collections import Counter
from prepareData import *
import sys
import os

features =  ['ROB','RISP','middle_at_bat','end_inning','no_hitter', 'inning',
              'shutout','perfect_game','variance','B_score_against',
              'B_score_for','B_strikeout_count','B_walk_count','B_hit_count','B_total_bases', 'B_pitch_number', 'paResult']

# ^ Global variable of features for isolation ^ #

def calcProbability(labels):
    # Modified book code
    total = float(len(labels))
    temp_count = {}
    for label in labels:
        if label not in temp_count:
            temp_count[label] = 0.0
        temp_count[label] += 1.0
    probability = []
    for item in temp_count.values():
        probability.append(item/total)
    return probability

def data_entropy(data):
    labels = [label for _, label in data]
    probabilities = calcProbability(labels)
    return entropy(probabilities)   

def entropy(probabilities):
    return sum(-p * math.log(p,2) for p in probabilities if p)         

def partition_by(inputs,attribute):
    groups = {}
    for datum in inputs:
        key = datum[0][attribute]
        if key not in groups:
            groups[key] = []
        groups[key].append(datum)
    return groups

def partition_entropy_by(inputs, attribute):
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

def partition_entropy(subsets):
    size = sum(len(subset) for subset in subsets)
    segEntropy = 0.0 
    for subset in subsets:
        indvSeg = data_entropy(subset) * ((float(len(subset))) / (float(size)))
        segEntropy += indvSeg
    return segEntropy

def labelData(trainingData, trainingLabels):
    labeledData = []
    for i in range(len(trainingLabels)):
        labeledData.append((trainingData[i], trainingLabels[i]))
    print labeledData
    return labeledData

def toLabel(data):
    labels = {}
    for val in data:
        temp = []
        for datum in data[val]:
            temp.append(datum[1])
        labels[val] = Counter(temp).most_common(1)[0][0]
    return labels

def featurePartitionTest(inputs, features):
    minFeature = None
    minVal = float('inf')
    for feature in features:
        entropy = partition_entropy_by(inputs, feature)
        if entropy <= minVal:
            minVal = entropy
            minFeature = feature
    return minFeature

## ^ DECISION STUMP CODE ENDS ^ ##
def maxSet(inputs):
    labels = []
    for datum in inputs:
        labels.append(datum[1])
    return Counter(labels).most_common(1)[0][0]


def buildTree(inputs, features, max_depth):
    data_set_entropy = data_entropy(inputs)
    
    #BASE CASE
    if max_depth <= 0 or features is None or data_set_entropy == 0.0:
        subtrees = [features, 0.0, {'decideOn':[labeledData for labeledData in inputs]}]
        return maxSet(inputs)

    #Modified code from book to incorporate info gain for printDiag func
    num_inputs = len(inputs)

    best_attribute = featurePartitionTest(inputs, features)
    currEntropy = partition_entropy_by(inputs, best_attribute) 
    infoGain = data_set_entropy - currEntropy

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in features if a != best_attribute]


    subtrees = [best_attribute, infoGain, {attribute_value: buildTree(subset, new_candidates, max_depth-1) for attribute_value, subset in partitions.iteritems()}]

    #End book code with above line modified

    return subtrees

def traverseForGuess(subtrees, guess):
    root = subtrees[0]
    child = subtrees[2]


    valToMatch = guess[root]     # Checks root current node against inputted guess 
    if isinstance(child[valToMatch], str):  
        #Check type comparison see if you are at decision node (str vs. next node) 
        return child[valToMatch] 


    #else recurse

    return traverseForGuess(child[valToMatch], guess)


def printDiag(subtrees, level):
    # RECURSION DEPTH
    numTabs = 0 + level

    # BEGIN PRINT
    print (numTabs*"  ") + "Split on " + str(subtrees[0]) + " (info gain = " + str(subtrees[1]) + "):"
    for feature in subtrees[2]:
        childByFeature = subtrees[2][feature]
        print numTabs * "  " + str(subtrees[0]) + "=" + str(feature) + "==>"
        if isinstance(subtrees[2][feature], str):  # CHECK FOR DECISION AND PRINT WITH LABEL IF LEAF
            print ((numTabs * "  ") + " Label = " + str(childByFeature))
        else:
            level += 1
            printDiag(childByFeature, level)
    pass

# ^ END LAB 7 CODE ^ #

def prepareData(file, flag):
    ''' 
    Takes in a specified filename and parses the data for use in decision tree. 
    (str) -> [(dict, bool)]
    '''
    # If you are running on the whole file as one 
    if flag == 'a':
        output = []
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                temp = {}
                label = None
                for key, value in row.iteritems():
                    # If data point is one of the features, place in output dictionary
                    if key in features:
                        temp[key] = value
                    # If last pitch of game by pitcher (label)
                    if key == 'last_pitch_game':
                        label = value   # True or False
                output.append((temp, label))

    # Generates a dictionary with key as pitcher ID and value as its input data for a tree 
    elif flag == 'p':
        output = {} # Above mentioned dict
        tempOutput = [] # Functionally the same as 'output' variable above 
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            first = reader.next()
            firstPass = True
            currPitchID = first['pitcherId']
            for row in reader:
                if row['pitcherId'] != currPitchID:
                    output[currPitchID] = tempOutput
                    tempOutput = []
                    currPitchID = row['pitcherId']
                
                temp = {}       # Initialize a temporary dict representing a data point of features
                label = None

                if firstPass:      # Makes sure to write the first row taken above in reader.next()
                    for key, value in first.iteritems():
                        if key in features:
                            temp[key] = value
                        if key == 'last_pitch_game':
                            label = value
                    firstPass = False
                    tempOutput.append((temp, label))

                for key, value in row.iteritems():
                    if key in features:
                        temp[key] = value
                    if key == 'last_pitch_game':
                        label = value
                tempOutput.append((temp, label))

    print "\nData Preparation Complete.\n"
    return output

def classify(tree, data,naive):
    """
    Classifies each datum by passing it through the decision tree.  

    Expects data to be a list.  Each datum in list is a feature vector (i.e., a dictionary)
    """
    guesses = []
    for datum in data:
        guess = traverseForGuess(tree, datum)
        if naive =='True':
            guess = 'False'
        guesses.append(guess)
    return guesses

def testCorrectness(trainingData,trainingLabels, testData, testLabels, tree):
    ''' 
    Tests the correctness of training vs test data guesses.
    ([list], [list], [list], [list], [list]) -> None
    '''
    #print "\nTraining..."
    guesses = classify(tree, trainingData,'False')
    correct = [guesses[i] == trainingLabels[i] for i in range(len(trainingLabels))].count(True)
    print str(correct), ("correct out of " + str(len(trainingLabels)) + " (%.1f%%) on training data.") % (100.0 * correct / len(trainingLabels))

    #print "Testing..."
    guesses = classify(tree, testData,'False')
    correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
    print str(correct), ("correct out of " + str(len(trainingLabels)) + " (%.1f%%) on testing data.") % (100.0 * correct / len(trainingLabels))

    toReturn = (correct, len(testLabels))

    #print "Naive..."
    guesses = classify(tree, testData,'True')
    correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
    print str(correct), ("correct out of " + str(len(trainingLabels)) + " (%.1f%%) using assumption of always false.") % (100.0 * correct / len(trainingLabels))

    return toReturn

def splitData(inputs, split):
    '''
    Takes in all of the data and splits the data into training and test portions based on the input "split" percentage.
    ([(dict,bool)]) -> [list], [list], [list], [list]
    '''
    trainingData = []
    trainingLabels = []
    testData = []
    testLabels = []
    split = split * .01       # Partitions the data set into size test(split percentage of total input) and train (remaining inputs)
    testSize = int(split * len(inputs))
    index = 0
    # While in test set...
    while index != testSize:        
        testData.append(inputs[index][0])
        testLabels.append(inputs[index][1])
        index += 1

    # While in train set... 
    while index != len(inputs):     
        trainingData.append(inputs[index][0])
        trainingLabels.append(inputs[index][1])
        index += 1

    return trainingData, trainingLabels, testData, testLabels

def testInputs(inputs, splitSize, treeDepth, printYN):
    '''
    Generalized function that takes in inputs, a size to split on, a tree depth, and a print flag and tests the input data.
    It then returns a tuple with the first int representing the numerator and second representing the denominator of the correct test data fraction. 
    ({dict}, int, int, str) -> (int, int)
    '''
    trainingData, trainingLabels, testData, testLabels = splitData(inputs, splitSize)
    tree = buildTree(inputs, features, treeDepth)
    #print "\nTree Generated.\n"

    if printYN == "Y":
        printDiag(tree, 0)
    testCorrect = testCorrectness(trainingData, trainingLabels, testData, testLabels, tree)
    return testCorrect

def testByPitcher(inputDict, depth):
    '''
    Takes in the dictionary with key as pitcher ID and the value as their parsed pitched data for use in tree. 
    Returns the list with all test scores of individual pitchers compared to test and training data. 
    See prepare data above for more insight.
    ({str: [{str: multiple}]}) -> [float]
    '''
    testScores = []
    for key, value in inputDict.iteritems():
        inputs = inputDict[key]
        testCorrect = testInputs(inputs, 50, depth, "N")
        testScores.append(testCorrect)
    return testScores

def calcAccuracy(testAnswers):
    ''' 
    Takes in the tuples representing test answers from training on test inputs. Returns the total value of (all num , all denoms)
    ([tuples]) -> tuple
    '''
    numer = 0
    denom = 0
    for item in testAnswers:
        numer += item[0]
        denom += item[1]
    return (float(numer), float(denom))


def main(argv):
    try:        
        file = str(argv[1])
    except IndexError:
        print "Please enter a filename."
        return
    try:
        flag = str(argv[2])
    except IndexError:
        print "Please enter a flag (a for entire data set, p for individual pithcer)."
        return
    try:
        try: 
            depth = int(argv[3])
        except IndexError:
            print "Please enter a depth (int 1-10)."
            return
    except ValueError:
        print "Please enter a valid depth (int 1-10)."
        return
    if depth > 10 or depth <= 0:
        print "Please enter a valid depth (int 1-10)."
        return
    # If you want to run the model on all pitcher data as one
    if flag == 'a':
        try:
            inputs = prepareData(file, flag)
        except IOError:
            print "Please enter a valid filename/path."
            return
        ## CHANGE THE Y TO N IF YOU DO NOT WANT TO PRINT OUT THE TREE (Or VV) ## 
        testCorrect = testInputs(inputs, 50, depth, "Y")
        testCorrect = float(testCorrect[0])/float(testCorrect[1])
        toPrint = (100.0 * testCorrect)
        print "Model accurate with " + str(toPrint) + "%% accuracy."

    # If you want to run the model on all pitcher data individually and then average the accuracy 
    elif flag == 'p':
        try:
            pithcerDict = prepareData(file, flag)
        except IOError:
            print "Please enter a valid filename/path."
            return            
        testCorrect = calcAccuracy(testByPitcher(pithcerDict, depth))
        toPrint = (100.0 * (testCorrect[0]/testCorrect[1]))
        print "Model accurate with " + str(toPrint) + "%% accuracy."

    else:
        print "Please enter a valid flag (a for entire data set, p for individual pithcers)."
        return 

if __name__ == "__main__":
   main(sys.argv)






