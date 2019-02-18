# Weekly Status Reports

Each week, please spend 5-10 minutes writing a brief status report.  This does not need to be highly detailed. Some examples are provided below that give some indication of the level of detail.

*Copy the template below for each subsequent week.  Please put the most recent week at the **TOP** of the page.*

## Week 7

Report for the week of 5/2 to 5/8/17

What did each project team member do this week?

- All: Discussed and decided on final direction

- Matt: Rewrote add_new_fields.py and added error handling to all files. Ran tests on individual models to gather data. Created PowerPoint and worked on write up. 

- Jeremy: Worked on visualizaitons and write up. 

- James: Implemented machine learning in sklearn for naive bayes and linear regression. Worked on write up/presentation.

Division of Labor:

- Matt: 33%

- James: 33%

- Jeremy: 33%


## Week 6

Report for the week of 4/25 to 5/1/17

What did each project team member do this week?

- All: Discussed and decided on final direction

- Matt: Worked on implementing model via a decision tree with James

- Jeremy: Wrote add_new_fields.py, which updates our data with columns containing the features we’ll use in our decision tree.  Also wrote graphs.py

- James: Worked on implementing model via a decision tree with Matt

Division of Labor:

- Matt: 33%

- James: 33%

- Jeremy: 33%


## Week 5

Report for the week of 4/18 to 4/24/17

What did each project team member do this week?

- All: Decided on new direction for end goal of project (removed focus on fatigue as overarching goal and instead how it plays into starter removal) and worked on presentation.

- Matt: Created PPT and met with Prof. in lab to gain feedback on visualizations and insight on the way forward. Presented in class and created new goals to accomplish over the coming weeks.

- Jeremy: Helped with presentation and data visualizations. Worked on new direction for the project. 

- James: Created new visualizations in Tableau that helped point out several flaws in our working model. 

Division of Labor:

- Matt: 40%

- James: 30%

- Jeremy: 30% 


## Week 4

Report for the week of 4/10/17 to 4/17/17.

What did each project team member do this week?

- All: Added pitch count values to each pitch and worked on graphing this data in order to uncover more interesting trends.  Worked on being able to isolate individual pitchers and calculate averages for these pitchers.


- Matt: Assisted with graphing and worked on function to aggregate average values by pitcher, inning, and stat in order to look for deviations from the norm by stat.

- James: Wrote sql commands to create csv files that have pitching data ordered chornologically by pitcher.  Wrote Add_Pitch_Count.py which adds a cummulative game pitch count to each pitch using the starters_only csv files.  Wrote Season_Pitch_Count.py which adds a cummulative season and past week pitch count to each pitch.  Added a funciton to graph.py which graphs a target variable over a given pitch count (e.g. releaseVelocity over season pitch count).  Experimented with Tableau and created some useful graphs. 

- Jeremy: Wrote isolateAndGraphPitcher.py, which allows the user to isolate specific pitchers, games, pitches, and thus calculate baseline average velocity, spin rate, and release point for a given pitch type for a given pitcher for a given start.  
Provide a rough estimate of the division of labor:

- Matt: 20%
- James: 40%
- Jeremy: 40%

What are the team's goals for next week?

Now that we can calculate baseline data, we’ll begin to build our model, which will determine fatigue based on changes in variance among pitches of the same type.

## Week 3

Report for the week of 4/3/17 to 4/10/17.

What did each project team member do this week?

- All: Determined what we’ll be focusing on moving forward.  Since we now have all the basic data fully cleaned and only containing starting pitchers, we decided that we’re going to focus on in-game fatigue, but will also analyze other aspects of fatigue (seasonal, in-inning) on the side.

- Matt: Cleaned up code from various files; generalized functions to accept all inputs and inputs from the command line; fixed errors in inning by inning graph and updated the cleanRelievers and graph files to more seamlessly work with data modeling. 

- James: Helped troubleshoot error in graph.  Also, before we determined a way to clean the relievers, James scraped starting pitching data from baseball-reference.com, and began writing code to join the two databases and identify starting pitchers by their names.  We realized their was too many discrepancies in naming to go forth with this method confidently.  

- Jeremy: Wrote clean_relievers.py, which creates new .csv files that contain data from only starting pitchers.  Also explored ways to clean relievers using baseball-reference.com before deciding it was a bad idea.

Provide a rough estimate of the division of labor:

- Matt: 45%
- James: 10%
- Jeremy: 45%

What are the team's goals for next week?

Our main goal is to graph individual variables (spin rate, velocity, change in release point) to see how they change as pitch count increases.  Once we’ve created these graphs and can see basic trends, we can begin to build a model that determines how fatigued a given pitcher is.

## Week 2

Report for the week of 3/27/17 to 4/3/17.

What did each project team member do this week?

- All: worked to determine which variables would be of interest and rough ideas about the types of questions we want to answer using this data.

- Matt: created the SQL database and python notebook

- James: Ran relevant SQL queries and outputed to csv files

- Jeremy: Started forming basic graphs

Provide a rough estimate of the division of labor:

- Matt: 40%
- James: 40%
- Jeremy: 20%

What are the team's goals for next week?

Our main goal is to start working with and manipulating the data in the csv files so that it has all of the relevant fields (for instance pitch number that game, pitch number that season, etc.)


## Week 1

Report for the week of 3/20/17 to 3/27/17.

What did each project team member do this week?

- Jeremy: I obtained the data set and created our proposal

Provide a rough estimate of the division of labor:

- Jeremy: 100%

What are the team's goals for next week?

Our main goal will be to determine exactly what we'll be researching/modeling.
