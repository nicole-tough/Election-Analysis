# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
import string
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# A. Iniialize a total vote counter
total_votes = 0 

# Declare a new list
candidate_options = []

# Declare dictionary for candidate:votes
candidate_votes = {}

# Declare winning candidate variable
winning_candidate = ""

# Declare a winning count variable
winning_count = 0 

# Declare a winning percent variable
winning_percentage = 0 

# Open the election results.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # B. Add to the total vote count.
        #total_votes = total_votes + 1
        total_votes += 1

         # Print the candidate name from each row
        candidate_name = row[2]

        # If candidate does not match existing candidate 
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking candidates votes
            candidate_votes[candidate_name] = 0
        # Add a vote for each count of candidates name, needs to be flush with for loop
        candidate_votes[candidate_name]+=1

# Write results to text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through candidate options
    for candidate_name in candidate_votes:
        # Count votes for each candidate
        votes = candidate_votes[candidate_name]
        # Calculate vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100 
        # Save candidate results to text file
        candidate_results = (
            f'{candidate_name} {vote_percentage:.1f}% ({votes:,})\n')
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, vote percentage, and candidate
        # Determine if votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning count = votes and winning percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set the winning candidate equal to the candidate name
            winning_candidate = candidate_name

        

                    
            
            

        



    # Print winning candidate summary
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)