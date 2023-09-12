import os
import csv

csvpath = "PyBank\\Resources\\budget_data.csv"
counter = 0
total = 0
previous_profit = None
profit_changes=[]
greatest_increase = 0
greatest_decrease = 0
greateat_increase_month = 0
greatest_decrease_month = 0



with open(csvpath) as budget_data:
    csvreader=csv.reader(budget_data)

    #skipping the header row
    csvheader = next(csvreader)
    

    for r in csvreader:
        counter = counter + 1
        total += int(r[1])
        date = r[0]

        if previous_profit is not None:
            change = int(r[1])-int(previous_profit)
            profit_changes.append(change)

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = date

            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = date


        
        previous_profit = r[1]
    average_change = sum(profit_changes) / len(profit_changes)
    
        



output=(
    f"Financial Analysis\n"
    f"{'-' * 20}\n"
    f"Total Months: {counter}\n"
    f"Total: $ {total}\n"
    f"Average Change: $ {round(average_change,2)}\n"
    f"Greatest Increase in Profit:   {greatest_increase_month}   ($  {greatest_increase})\n"
    f"Greatest Decrease in Profits:  {greatest_decrease_month}   ($ {greatest_decrease})\n"
)

print(output)

with open("PyBank/analysis/financial Analysis.txt" , "w") as text_file:
    text_file.write(output)



