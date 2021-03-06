import os
import csv

# Path to retrieve data from the Resources file
budget_data_path = os.path.join('Resources','budget_data.csv')

# Read in the csv data
with open(budget_data_path,'r') as budget_data_file:
    #Split data on commas - using csv reader function - csv.reader()
    budget_data_reader = csv.reader(budget_data_file, delimiter=',')

    #Skip header
    next(budget_data_reader)

    # set variables
    total_mos = 0
    total_pl = 0
    pl_chg = []
    list_mos = []

    # Loop through reader data
    for row in budget_data_reader:

        # Calc total mos
        total_mos = total_mos + 1

        # calc total profit and loss + the integer that is in column - use row as in the index (running total of P/L)
        total_pl = total_pl + int(row[1])
        month = row[0]

        # collected the columns of p/l - this will be a list of P/L column use append and the index for row, and read in the dates will be the second column
        pl_chg.append(int(row[1]))
        list_mos.append(row[0])
        
        # calculating the change in profit and loss using a list to store the difference/change
        diff_column = []

        # loop through list of p/l to calcualte difference in each row 
        for i in range(0,len(pl_chg)-1):
            difference = pl_chg[i+1] - pl_chg[i]
            diff_column.append(difference)


            # calculate the average change in pl
            # look for zero denominator once you have
            # the zero_exception then assign 0
            try:
                avg_chg_pl = sum(diff_column)/len(diff_column)
            except ZeroDivisionError:
                avg_chg_pl = 0
                       
            # calculate the maximum - greatest increase in difference column/list (pl change)
            greatest_increase = max(diff_column)
        
            # store the month for greatest increase
            greatest_mo = diff_column.index(greatest_increase)

            # calculate the greatest decrease in difference column/list (pl change)
            greatest_decrease = min(diff_column)

            # store the month for greatest decrease
            greatest_decrease_mo = diff_column.index(greatest_decrease)

    # Print to screen financial analysis
    print(f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total Months: {total_mos}\n"
        f"Total: {total_pl}\n"
        f"Average Change: {avg_chg_pl}\n"
        f"Greatest Increase in Profits: {list_mos[greatest_mo +1]} ({greatest_increase})\n"
        f"Greatest Decrease in Profits: {list_mos[greatest_decrease_mo +1]}({greatest_decrease})")

    # Print to txt file in Analysis folder
    output_path = os.path.join("analysis","FinancialAnalysis.txt")
    with open(output_path, 'w') as txtfile:
        txtfile.write(f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total Months: {total_mos}\n"
        f"Total: {total_pl}\n"
        f"Average Change: {avg_chg_pl}\n"
        f"Greatest Increase in Profits: {list_mos[greatest_mo +1]} ({greatest_increase})\n"
        f"Greatest Decrease in Profits: {list_mos[greatest_decrease_mo +1]}({greatest_decrease})")
            
        
                       



        
         




     