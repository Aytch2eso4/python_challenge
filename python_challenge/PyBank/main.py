
import os

# Module for reading CSV files
import csv

#csv file will be in Resources dir at our script level
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# The dataset is composed of two columns: Date and Profit/Losses. 

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    num_months = 0    #init to 0
    sumPandL = 0
    i = 0
    prior_month_value = ""
    total_change = 0
    max_pos_change = 0
    max_neg_change = 0
    max_pos_change_month = ""
    max_neg_change_month = ""
    sum_of_monthly_changes = 0


    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        num_months = num_months + 1      # will determine the num of months in this entire period (REQUESTED)
        sumPandL = sumPandL + int(row[1])    # will determine the net total amount of Profit/Losses over the period (REQUESTED)
        i = i + 1
        if (prior_month_value != ""):
            monthly_change = int(row[1]) - int(prior_month_value)
            if monthly_change > max_pos_change:
                max_pos_change = monthly_change     # will determine the greatest inc in profits
                max_pos_change_month = row[0]     # and its month
            elif monthly_change < max_neg_change:
                max_neg_change = monthly_change     # will determine the greatest decr in profits
                max_neg_change_month = row[0]     # and its month
            
            sum_of_monthly_changes = sum_of_monthly_changes + monthly_change   # sum up all the changes
        prior_month_value = row[1]      #set it now
            
#determine the average of the changes in "Profit/Losses" over the entire period
average_change = round(sum_of_monthly_changes / (i -1),2)

print("\nFinancial Analysis") 
print("-----------------------") 
print("Total Months: " + str(i))
print("Total: $" + str(sumPandL))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_pos_change_month) + " ($" + str(max_pos_change) + ")")
print("Greatest Decrease in Profits: " + str(max_neg_change_month) + " ($" + str(max_neg_change) + ")")
print("")
foutname = "fin_analysis_budget_data.txt"
print("Printing this financial analysis to: " + str(os.getcwd()) + "/" + foutname)

#write the Financial Analysis to a file, a text file, not a csv file
with open(foutname, 'w') as file_object:
    file_object.write("Financial Analysis\n")
with open(foutname, 'a') as file_object:
    file_object.write("-----------------------\n")
    file_object.write("Total Months: " + str(i) + "\n")
    file_object.write("Total: $" + str(sumPandL) + "\n")
    file_object.write("Average Change: $" + str(average_change) + "\n")
    file_object.write("Greatest Increase in Profits: " + str(max_pos_change_month) + " ($" + str(max_pos_change) + ")\n")
    file_object.write("Greatest Decrease in Profits: " + str(max_neg_change_month) + " ($" + str(max_neg_change) + ")\n")
    file_object.write("\n")
print("\nFinished!")   
        
