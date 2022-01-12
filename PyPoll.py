
#Need to retrieve data from dataset in CSV file
#1. total number o votes
#2. A complete list o candidates who received votes
#3. % of votes each candidate won
#4. Total num of votes each can won
#5. the winner of the election based on popular vote

#imports
import csv
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.

with open(file_to_load) as election_data:

    # Print the file object.
    #print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
    
# U
# sing the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Counties in the Election\n-------------------------\n")
    # Write three counties to the file.
#    txt_file.write("Arapahoe\nDenver\nJefferson")