# python-challenge

# Project 1: Financial Records Analysis (PyBank)

# Objective

The goal of this projects is to create a Python Script that analyze the financial records in 'budget_data.csv' file and calculate the following values  :
1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
4. The greatest increase in profits (date and amount) over the entire period

# Files 
1. The dataset containing financial records : `Resources/budget_data.csv`
2. The output file that contains analysis results : `analysis/budget_analysis.txt`
3. The Python file to run the analysis : `PyBank.py`

# Instructions
1. Place the `budget_data.csv` file in the `Resources` directory.
2. Run the `PyBank.py` script to perform the analysis.
3. The results will be printed in the terminal and saved to `budget_analysis.txt` in the `analysis` directory.

# Output
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

# Project 2: Election Results Analysis (PyPoll)

# Objective
The goal of this projects is to create a Python Script that analyze the election data in 'election_analysis.csv' file and calculate the following values  :
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. Total number of votes each candidate won
5. The winner of the election based on popular vote

# Files 
1. The dataset containing election data : `Resources/election_data.csv`
2. The output file that contains analysis results : `analysis/election_analysis.txt`
3. The Python file to run the analysis : `PyPoll.py`

# Instructions
1. Place the `election_data.csv` file in the `Resources` directory.
2. Run the `PyPoll.py` script to perform the analysis.
3. The results will be printed in the terminal and saved to `election_analysis.txt` in the `analysis` directory.

# Output

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)

Diana DeGette: 73.812% (272892)

Raymon Anthony Doane: 3.139% (11606)

-------------------------
Winner: Diana DeGette
-------------------------