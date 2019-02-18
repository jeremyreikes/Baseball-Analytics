# COSC 480 DS Project - A Sigh Of Relief

## Data Collection

Project data can be obtained with the following commands:

    curl -O https://s3.amazonaws.com/misc.trumedianetworks.com/hackathons/mlb/2017/mlb-hackathon-2017-samples.zip
    curl -O https://s3.amazonaws.com/misc.trumedianetworks.com/hackathons/mlb/2017/mlb-hackathon-2017.zip
    
Make sure to unarchive the directories and place these files into the working directory of your project. 

## Data Preparation

The psql database can be created and initialized by running the following commands:

    psql baseball -f create.sql | psql baseball

First, clean out the relievers from each dataset by running the cleanRelievers.py file. You may pass in all of the files at the same time as arguments from the command line as so:

    python cleanRelievers.py file/path/1 file/path/2 # and so on
    
Then run the add_new_fields.py file in order to add additional features to the datasets you just created above (startersOnly_201x.csv) based on existing information:

    python add_new_fields.py filename flag inning 
    
with the flag being 'all' if you want to generate a file for the entire dataset, or a specified pitcherID if you want to create a new dataset for a specific pitcher. The inning, in this case, is a starting point from which to generate the data, with, for example, an inning set to 3 outputting a file with pitches from the 3rd inning to the end of the appearence. 

Additionally, you may run Add_Pitch_Count.py and Season_Pitch_Count.py on the original datasets to create new datasets that keep track of given pitch counts by game and seson. These can be used in visualiztion.  

## Visualizations

Now its time to visualize and analyze the data. 

To view graphs based on the data (coded and documented in graphs.py), open the ipython notebook and run the graphing commands. Make sure you have specified the filenames for which you wish to create graphs (ex. new_fields_all_startersOnly_2016.csv) within the notebook.

## Machine Learning Analysis
  
To analyze the data, there are several options: a decision tree, linear regression, naive bayes. 

### Tree

To use the decision tree technique, run the following command:
    
    python tree.py filename flag depth 
 
with the flag being a or p (a for all pitchers simultaneously, p for pitchers individually, averaged at the end) and depth being the depth of the tree. 

This will print out training and testing scores for the data, as well as results for the assumption always being false. You can also print out the tree by passing in "Y" to the printYN parameter of the testInputs function. 

### Linear Regression and Naive Bayes

To run linear regression on the dataset, run the following command:

    python machine_learn.py flag feature1 feature2 ... 
    
 with the flag 'lr' and features as space seperated variables (ex. end_inning paResult ROB RISP) for linear regression and 'nb' and features as space seperated variables (ex. end_inning paResult ROB RISP) for naive bayes. 
 
 This will print out the accuracy of the model for the given features and the percent this model classifies correctly and the percent the assumption always false classifies correctly.
