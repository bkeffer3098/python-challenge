#Importing the operating system and csv capailities
import os, csv

total_votes = 0
candidates = []
#Candidate Votes has to be a dictionary to make key pair data
candidate_votes = {}

csvpath = os.path.join("C:\\Users\\Brian Keffer\\GW Bootcamp\\python-challenge\\PyPoll\\Resources\\election_data.csv")

with open(csvpath, encoding= "UTF-8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    #Skipping the header row
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[candidate] = 0

        candidate_votes[candidate] += 1
#Outside of the iteration and after reading
# Percents
percentage = {key: round(value / total_votes * 100, 3) for key,value in candidate_votes.items()}

winner = max(candidate_votes, key = candidate_votes.get)

output_file = os.path.join("C:\\Users\\Brian Keffer\\GW Bootcamp\\python-challenge\\PyPoll\\Analysis\\Results_PyPoll.txt")
with open(output_file, 'w') as text_file:

    #\n means to end line
    four_lines = (f'Election Results\n'
                  '-----------------------------\n'
                  f'Total Votes: {total_votes}\n'
                  '-----------------------------\n')
    #Must be printed in the terminal
    print(four_lines)
    text_file.write(four_lines)

    for key, value in candidate_votes.items():

        votes_received = (f'{key}: {percentage[key]}% ({value})\n')
        print(votes_received)
        text_file.write(votes_received)
    
    winner_lines = ('-----------------------------\n'
                    f'Winner: {winner}\n'
                    '-----------------------------\n')
    print(winner_lines)
    text_file.write(winner_lines)

#Checking work with prints

#print(total_votes)
#print(candidates)
#print(candidate_votes)
#print(percentage)
#print(winner)