#import file
import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

# Assign values to variables 
total_months = []
net_total_amount = []
average_change = []
previous_amount = None
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0   
greatest_decrease_month = 0

# Read in the CSV file
with open(budget_data) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        net_total_amount.append(int(row[1]))
        if previous_amount != None:
            average_change.append(int(row[1]) - previous_amount)
        previous_amount= int(row[1])
        
# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length


# Test your function with the following:
print(f"Total Months: {len(total_months)}")
print(f'Average Change: ${round(average(average_change),2)}')

# Find net total amount of "Profit/Loss" over entire period
x = sum(net_total_amount)
print(f'Total Profits/Losses: ${x}')

# Find greatest increase in profits (date and amount) over the entire period
max_increase_amount = max(average_change)
max_decrease_amount = min(average_change)

max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1

print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_amount))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_amount))})")


output_file = os.path.join('Analysis', 'Financial_Analysis.txt')

with open(output_file,"w") as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {len(total_months)}\n")
    txtfile.write(f"Total: ${sum(net_total_amount)}\n")
    txtfile.write(f"Average Change: ${round(average(average_change),2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_amount))})\n")
    txtfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_amount))})\n")
