# imports (files)
import os
import csv

# import data (path)
file_to_open = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("results","election_results.txt")

# declare global variables
# Total # of votes cast
total_votes = 0


# if using functions create 

# start loop - with open
with open(file_to_open, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # This skips the first row of the CSV file.
    next(csvreader)

    # List of candidates
    candidates = []

    # dictionary
    candidate_votes = {}
    for row in csvreader:
        # do stuff with rows...
        # total number of votes cast 
        total_votes = total_votes + 1

        # List of candidates that received votes
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            # Total No of votes and % of Total votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    # open file to print up here, you will need to tab everything in
    print(f"Election Results \n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
    # this needs to be while we are are in the candidates and do we need to sort the data by candidate
    # percentage is = to candidate_votes / total_votes 
    # percentage_votes = total_votes / candidate_votes
    # print(candidate_votes)
    for candidate in candidates:
        votes = candidate_votes.get(candidate)
        percentage_votes = (candidate_votes.get(candidate)/total_votes) * 100
        print(f"{candidate}: ({candidate_votes.get(candidate)}) {percentage_votes:.2f}% \n")
        
        # add operator functions in code
    import operator
    winner_elec = max(candidate_votes.items(), key=operator.itemgetter(1)) [0]
    print(f"-------------------------\n"
    f"Winner: {winner_elec} \n"
    f"-------------------------\n")
    # print(percentage_votes)
    # print(votes)
    # Print to txt file in Analysis folder
    with open(output_path, 'w') as txtfile:
        txtfile.write(f"Election Results \n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
        for candidate in candidates:
            votes = candidate_votes.get(candidate)
            percentage_votes = (candidate_votes.get(candidate)/total_votes) * 100
            txtfile.write(f"{candidate}: ({candidate_votes.get(candidate)}) {percentage_votes:.2f}% \n")
        import operator
        winner_elec = max(candidate_votes.items(), key=operator.itemgetter(1)) [0]
        txtfile.write(f"-------------------------\n"
        f"Winner: {winner_elec} \n"
        f"-------------------------\n")