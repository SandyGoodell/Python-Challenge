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
