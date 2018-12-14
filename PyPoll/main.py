# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# ## Hints and Considerations

# Consider what we've learned so far. To date, we've learned how to import modules like `csv`;
#  to read and write files in various formats; to store contents in variables, lists, and dictionaries;
#  to iterate through basic data structures; and to debug along the way. Using what we've learned,
#  try to break down you tasks into discrete mini-objectives. This will be a _much_ better course of action
#  than attempting to Google Search for a miracle.

# As you will discover, for some of these challenges, the datasets are quite large. 
# This was done purposefully, as it showcases one of the limits of Excel-based analysis.
#  While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in
#  Python can provide us with more robust options for handling "big data".

# Your scripts should work for each dataset provided. Run your script for each dataset separately to
#  make sure that the code works for different data.

# Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

# * Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." Come prepared to show your effort and thought patterns, we'll be happy to help along the way.

#* Always commit your work and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.
# ******************************************************************************
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'r') as file_handler:
    PyPoll = file_handler.read()
#print(PyPoll)
    # for row in PyPoll:
    #    # process each row
    #    writer.writerow(row)
##############The total number of votes cast#####################
total_votes = 0
PyPoll = {'Voter_ID': "12864552", 'County': "Marsh", 'Candidate': "Khan"}
    for row in PyPoll:
       total_votes = total_votes + 1
# print("The total votes is " + str(total_votes))

################A complete list of candidates who received votes
Vote_getter = []
Vote_count = 0

#print(list(set(PyPoll.values())))
#Cand = candidate value
#print(PyPoll['Candidate'])
# print(PyPoll.items())
# #print(PyPoll.values())
# #print(PyPoll.keys())
for row in PyPoll:
    if row in Vote_getter:
        pass
    else:
        Vote_getter.append(row):

number_vote_getters = len(Vote_getter)
number_vote_getters = n_v_g

for row in PyPoll:
    if row = Vote_getter

# for votes in Vote_getter:
#     print(votes)
    
#print(f'{PyPoll["Candidates"]}')
#     Vote_getter.append(Candidate)
#     print(Vote_getter)
# Vote_getter = set()
# for dic in PyPoll:
#    for val in dic.values():
#       Vote_getter.add(val)
Print(Vote_getter)
#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
filename = 'Pybank_output.txt'
with open(filename,'w') as file_object:
    file_object.write()