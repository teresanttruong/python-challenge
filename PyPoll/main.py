# Import csv file
import os
import csv
from collections import Counter

# Set path for file
csvpath = r"C:\Users\Owner\Data_Analytics\Module_3_Python\python-challenge\PyPoll\Resources\election_data.csv"

def votescsv(csvpath):
    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        votes = [row[2] for row in reader]
        return votes
    
votes = votescsv(csvpath)

print("Election Results")
print(" ")
print("------------------------------")
print(" ")

# The total number of votes cast
total_votes = len(votes)
print("Total Votes: ", total_votes)
print(" ")

# A complete list of candidates who received votes
unique_candidates = list(set(votes))
print("------------------------------")
print(" ")

# The percentage of votes each candidate won and total number of votes per candidate
vote_counts = Counter(votes)
for candidate, count in vote_counts.items():
    percentage = (count/total_votes) * 100
    print(f"{candidate} : {percentage:.2f}% ({count} votes)")
print(" ")
print("------------------------------")
print(" ")

# The winner of the election based on popular vote
winner = vote_counts.most_common(1)[0][0]
print("Winner: ", winner)
print(" ")
print("------------------------------")

# Set variable for output file
folder_path = "..\home"
output_file = "PyPoll_Final.txt"
output_path = os.path.join(folder_path, output_file)

# Open the output file
with open(output_path, "w") as output_file:
    output_file.write("Election Results | ")
    output_file.write("Total Votes:" + str(total_votes) + " | ")
    output_file.write(f"{candidate} : {percentage:.2f}% ({count} votes) | ")
    output_file.write("Winner: " + str(winner) + " | ")