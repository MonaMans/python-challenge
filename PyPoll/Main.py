#import file
import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

# Assign values to variables 
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Read in the CSV file
with open(election_data) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        # For total number of votes cast 
        total_votes += 1
        #For number of votes each candidate won
        if (row[2] =="Khan"):
            khan_votes +=1
        elif (row[2]=="Correy"):
            correy_votes +=1
        elif (row[2]=="Li"):
            li_votes +=1
        elif (row[2]=="O'Tooley"):
            otooley_votes +=1

        #Percentage of votes each candidate won
        khan_percent = khan_votes/total_votes
        correy_percent = correy_votes/total_votes
        li_percent = li_votes/total_votes
        otooley_percent = otooley_votes/total_votes

        #Winner of the election based on popular vote
        #Create 2 lists, zip the lists together, use max function to determine winner
        candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
        vote_list = [khan_votes, correy_votes, li_votes, otooley_votes]
        dict_candidate_list_vote_list = dict(zip(candidate_list,vote_list))
        key = max(dict_candidate_list_vote_list, key=dict_candidate_list_vote_list.get)

#Print output
print("Election Results")
print("---------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("---------------------------------------------------------")
print(f'Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})')
print(f'Correy: {round((correy_votes/total_votes)*100,3)}% ({correy_votes})')
print(f'Li: {round((li_votes/total_votes)*100,3)}% ({li_votes})')
print(f"O'Tooley: {round((otooley_votes/total_votes)*100,3)}% ({otooley_votes})")
print("---------------------------------------------------------")
print(f"Winner: {key}")
print("---------------------------------------------------------")

#Write output file for the analysis
output_file = os.path.join('Analysis', 'Election_Results.txt')

with open(output_file,"w") as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})\n")
    txtfile.write(f"Correy: {round((correy_votes/total_votes)*100,3)}% ({correy_votes})\n")
    txtfile.write(f"'Li: {round((li_votes/total_votes)*100,3)}% ({li_votes})\n")
    txtfile.write(f"O'Tooley: {round((otooley_votes/total_votes)*100,3)}% ({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {key}\n")
    txtfile.write(f"---------------------------\n")



