import csv
import sys
from sklearn import linear_model
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import GaussianNB

import numpy as np



def preprocess(filename,fields):
    with open(filename,'r') as f:
        reader = csv.DictReader(f)
        pitches_array = []
        res_array = []
        for pitch in reader:
            desired_pitch = {}
            for field in pitch.keys():
                if field == 'last_pitch_game':
                    if pitch[field]=='False':
                        res_array.append(0)
                    else:
                        res_array.append(1)
                if field in fields:
                    if field in ['score_against','score_for','strikeout_count','walk_count','hit_count','total_bases','pitch_number']:
                        desired_pitch[field] = int(pitch[field])
                    else:
                        desired_pitch[field] = pitch[field]
            pitches_array.append(desired_pitch)
        return pitches_array,res_array

def log_reg(pitches_array,res_array):
    vec = DictVectorizer()
    Xs = vec.fit_transform(pitches_array)

    length  = len(pitches_array)
    X_train = Xs.toarray()[:length/2]
    Y_train = res_array[:length/2]
    X_test = Xs.toarray()[length/2:]
    Y_test = res_array[length/2:]

    logistic = linear_model.LogisticRegression()

    logistic.fit(X_train,Y_train)
    res_dict = {}
    for i in range(len(logistic.coef_)):
        res_dict[vec.feature_names_[i]] = logistic.coef_[i]

    lg_wrong_count = 0.0
    lg_always_false_count = 0.0

    for i in range(len(logistic.predict(X_test))):
        if logistic.predict(X_test)[i]>0.5:
            prediction = 1
        else:
            prediction = 0
        if prediction != Y_test[i]:
            lg_wrong_count+=1
        if Y_test[i] == 1:
            lg_always_false_count +=1

    print "Logistic Regression"
    print 'correct pct:', 1-(lg_wrong_count/len(X_test))
    print 'all false correct pct:', 1-(lg_always_false_count/len(X_test))



def naive_bayes(pitches_array,res_array):

    vec = DictVectorizer()
    Xs = vec.fit_transform(pitches_array)

    length  = len(pitches_array)
    X_train = Xs.toarray()[:length/2]
    Y_train = res_array[:length/2]
    X_test = Xs.toarray()[length/2:]
    Y_test = res_array[length/2:]

    gnb = GaussianNB()
    y_pred = gnb.fit(X_train,Y_train).predict(X_test)


    wrong_count =0.0
    false_wrong_count = 0.0
    for i in range(len(y_pred)):
        if y_pred[i] != Y_test[i]:
            wrong_count +=1
        if Y_test[i]==1:
            false_wrong_count +=1

    print "Naive Bayes"

    print 'correct pct:',1-wrong_count/len(y_pred)
    print 'all false correct pct:',1-false_wrong_count/len(y_pred)




def main(argv):
    try:
        filename = str(argv[1])
        flag = str(argv[2])
    except IndexError:
        print "Please enter valid flags (filename, flag, features)."
        return
    fields = []
    for i in range(len(argv)):
        if i > 2:
            fields.append(str(argv[i]))
    if len(fields) == 0:
        raise Exception("Please enter features.")
    try:
        result_array = preprocess(filename,fields)
    except IOError:
        print "Please enter a valid filename/path."
        return
    pitches_array = result_array[0]
    tag_array = result_array[1]
    if flag == 'lr':
        log_reg(pitches_array,tag_array)
    elif flag == 'nb':
        naive_bayes(pitches_array,tag_array)
    else:
        print "Please enter a valid flag, 'lr' for linear regression or 'nb' for naive bayes."


if __name__ == '__main__':
    main(sys.argv)

