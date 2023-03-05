#test
"""PY Poll Code"""
#read in csv
import os
import csv

file_path = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#create lists
votes_list = []
candidate_list = []
candidates = []
percentages = []


with open(file_path) as file:

    election_datafile = csv.reader(file, delimiter= ',')

    election_headers = next(election_datafile)

    for row in election_datafile:
        # The total number of votes cast (code works)
        votes_list.append(row[0])
        votes_list= [int(row) for row in votes_list]
        total_votes = len(votes_list)

#         # A complete list of candidates who received votes (code works)
#         candidate_list.append(row[2])
#         candidates = list(dict.fromkeys(candidate_list))

#         # The percentage of votes each candidate won  (code works)
#         # count_chuck = candidate_list.count('Charles Casper Stockham')
#         # count_di = candidate_list.count('Diana DeGette')
#         # count_weirdo = candidate_list.count('Raymon Anthony Doane')

#         # vote_counts = [count_chuck, count_di, count_weirdo]
#         vote_counts = [(candidate_list.count('Charles Casper Stockham')), (candidate_list.count('Diana DeGette')), (candidate_list.count('Raymon Anthony Doane'))]

#         # percent = round(vote_counts/total_votes * 100, 3)
#         percent = [(x/total_votes * 100) for x in vote_counts]
#         percentages.append(percent)

    

#         # percent_chuck = round(count_chuck/total_votes * 100, 3)
#         # percent_di = round(count_di/total_votes * 100, 3)
#         # percent_weirdo = round(count_weirdo/total_votes * 100, 3)

    
    print('Election Results')
    print('--------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------------')
#     print(candidates)
#     print('--------------------------------------')
#     print('winner')
#     print('--------------------------------------')
#     print(vote_counts)
#     print(percent)
#     print(percentages)

# rigged = zip(candidate_list, votes_list)

# output_file = os.path.join("election_results.csv")

# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)
#     writer.writerow(["Candidates", "Votes"])
#     writer.writerows(rigged)




# The total number of votes each candidate won

# The winner of the election based on popular vote.