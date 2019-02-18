import matplotlib.pyplot as plt
import graphs
import csv
from collections import defaultdict
from collections import OrderedDict

def get_axial_data(filename):
    '''
    Takes in a filename and returns a list containing the xs and ys for each feature, along with the feature name
    (str) -> [[[int], [int], [int], [int], (str)], [[int], [int], [int], [int], (str)]...]
    '''
    with open(filename, 'r') as f:
        features = ['ROB', 'RISP', 'middle_at_bat', 'end_inning',
                    'no_hitter', 'shutout', 'perfect_game']
        axial_data = []

        for feature in features:
            input = csv.DictReader(f)
            pitch_numbers_and_counts = dict()
            total_pitch_numbers_and_counts = dict()
            feature_counts = dict()
            total_feature_counts = dict()
            # create dictionaries containing pitch data for features and all pitches
            for pitch in input:
                count = int(pitch['pitch_number'])
                last_pitch = pitch['last_pitch_game']
                if last_pitch == 'True':
                    if count in pitch_numbers_and_counts.keys():
                        pitch_numbers_and_counts[count] += 1
                    else:
                        pitch_numbers_and_counts[count] = 1
                if count in total_pitch_numbers_and_counts.keys():
                    total_pitch_numbers_and_counts[count] += 1
                else:
                    total_pitch_numbers_and_counts[count] = 1
                if pitch[feature] == 'True':
                    if last_pitch == 'True':
                        if count in feature_counts.keys():
                            feature_counts[count] += 1
                        else:
                            feature_counts[count] = 1
                    if count in total_feature_counts.keys():
                        total_feature_counts[count] += 1
                    else:
                        total_feature_counts[count] = 1

            #initialize xs and ys for all pitches

            pitch_count = OrderedDict(sorted(pitch_numbers_and_counts.items()))  # count pulled
            pitch_count_totals = OrderedDict(sorted(total_pitch_numbers_and_counts.items()))  # total count
            pitch_graph = dict.fromkeys(pitch_count.keys())
            for pitch_number in pitch_graph.keys():
                pitch_graph[pitch_number] = float(pitch_count[pitch_number]) / float(
                    pitch_count_totals[pitch_number])
            xs = pitch_graph.keys()
            ys = pitch_graph.values()

            #initialize xs and ys for all pitches given a specific feature
            feature_count = OrderedDict(sorted(feature_counts.items()))
            feature_count_totals = OrderedDict(sorted(total_feature_counts.items()))
            feature_graph = dict.fromkeys(feature_count_totals.keys())
            for pitch_number in feature_graph.keys():
                if pitch_number in feature_count.keys():
                    feature_graph[pitch_number] = float(feature_count[pitch_number])/float(feature_count_totals[pitch_number])
                else:
                    feature_graph[pitch_number] = 0
            
            xs2 = feature_graph.keys()
            ys2 = feature_graph.values()

            axial_data.append([xs, ys, xs2, ys2, feature])
            f.seek(0)
    return axial_data

def initialize_graphs(filename):
    '''
    Takes in axial data and displays feature graphs in graphs.ipynb
    [[[int], [int], [int], [int], (str)], [[int], [int], [int], [int], (str)]...] -> None
    '''
    axial_data = get_axial_data(filename)
    features = {'ROB' : [(0, 116), (0, 0.4), 'ROB'], 'RISP' : [(0, 116), (0, 0.4), 'RISP'],
                'middle_at_bat' : [(0, 116), (0, 0.4), 'Middle of the at bat?'],
                'end_inning' : [(15, 116), (0, 0.4), 'End of the inning?'],
                'no_hitter' : [(0, 100), (0, 1), 'No hitter?'],'shutout' : [(0, 116), (0, 0.4), 'Shutout?'],
                'perfect_game' : [(0, 80), (0, 0.2), 'Perfect game?']}
    for index, data in enumerate(axial_data):
        xs = data[0] # for totals
        ys = data[1]
        xs2 = data[2] # for features
        ys2 = data[3]
        feature = data[4]
        feature_name = features[feature][2]
        # create a new figure for each graph
        plt.figure(index+1)
        #plot data
        plt.plot(xs, ys, label='Baseline')
        plt.plot(xs2, ys2, label=feature_name)
        xlims = features[feature][0]
        ylims = features[feature][1]
        plt.xlim(xlims[0], xlims[1]) #uncomment this line to change x limits of the graph
        plt.ylim(ylims[0], ylims[1]) #uncomment this line to change y limits of the graph
        plt.xlabel('Pitch number')
        plt.ylabel('% Chance Removed')
        plt.title('Effect of feature ' + feature)
        plt.legend(loc='upper left')
        plt.show()
