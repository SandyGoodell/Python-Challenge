# Python-Challenge
## PyBank
Script for analyzing financial data. File data was budget_data.csv. The data set had two columns: Date and Profit/Loss. The following calculations were made

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

One set of code was helpful that I found on stackoverflow was the division by zero error
'try:
    avg_chg_pl = sum(diff_column)/len(diff_column)
 except ZeroDivisionError:
    avg_chg_pl = 0'
## PyPoll
Script for analyzing the votes and candidates of election_data.csv The had 3 columns, Voter Id, County and Candidate.

The following calculations were made:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

