# The Data we need to Retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recevied votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on pupular vote.

import datetime
now = datetime.datetime.now()
print("The time right now is ", now)

import csv
file_to_load = '/Users/gobinaththangaiya/Documents/GitHub/ELection_Analysis/Resource/election_results.csv'

# Open the election results and read the file
election_data = open(file_to_load, 'r')

# To do: perform analysis
print(election_data)

# Close the file
election_data.close()

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
