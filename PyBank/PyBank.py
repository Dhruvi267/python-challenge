# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
change = []
date = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    profit_losses = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Track the net change
        total_net += int(row[1])

        # Calculate the net change in "Profit/Losses" from the previous month 
        net_change = int(row[1]) - profit_losses 
        change.append(net_change) 
        date.append(row[0]) 
        
        # Update the previous profit/losses to the current row's profit/losses 
        profit_losses = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(change)
        greatest_increase_date = date[change.index(greatest_increase)]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(change)
        greatest_decrease_date = date[change.index(greatest_decrease)]



# Calculate the average net change across the months
average_change = sum(change) / len(change)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n" 
    f"Total Months: {total_months}\n" 
    f"Total: ${total_net}\n" 
    f"Average Change: ${average_change:.2f}\n" 
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n" 
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n" 
    )


# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
