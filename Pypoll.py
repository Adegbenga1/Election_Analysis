import csv
import os
# Add a variable to load a file from a path.
csvpath = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
txtpath = os.path.join("Analysis","election_analysis.txt")
#Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
# 1: Create a county list and county votes dictionary.
County_list = []
County_Votes = {}
# Track the winning candidate, vote count and percentage (Winning Candidate and Winning Count Tracker)
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# 2: Track the largest county and county voter turnout.
Largest_county_Vote = ""
Largest_County_turnout = 0
# Open the CSV # Read the csv and convert it into a list of dictionarie
with open(csvpath) as election_results:
    csv_reader = csv.reader(election_results)
    for row in csv_reader:
        print(row[:3])
        break
    else:
        print("Not found")  
 # Print each row in the CSV file.
# Print each row in the CSV file. Get the candidate name from each row.
    for row in csv_reader:
        total_votes += 1
       # 3. Print the total votes.
# Print the candidate name from each row.
        candidate_name = row[2] 
         # 3: Extract the county name from each row.
        County_name = row[1]
 # Add the candidate name to the candidate list. If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if County_name not in County_list:
            # 4b: Add the existing county to the list of counties.
            County_list.append(County_name)
            # 4c: Begin tracking the county's vote count.
            County_Votes[County_name] = 0
        # 5: Add a vote to that county's vote count.
        County_Votes[County_name] += 1
with open(txtpath, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    txt_file.write(election_results)
    County_Result= (
                f"\nCounty Result\n" 
                f"-------------------------\n")
                # f"{county }: {county_vote_percent}%, {county_vote} Total Vote ")
    print(County_Result, end="")    
    # 6e: Save the county votes to a text file.
    txt_file.write(County_Result)
      # 6a: Write a for loop to get the county from the county dictionary.  
    for county in County_list:
    # 6b: Retrieve the county vote count.
        current_votes = County_Votes[county] 
    # 6c: Calculate the percentage of votes for the county.
        county_vote_percent = (current_votes/total_votes) *100
    #txtpath.write(f"{County_name }: {county_vote_percent :.1f}% ({county_vote:,})\n")
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if  current_votes > Largest_County_turnout:
            Largest_County_turnout = current_votes
            Largest_county_Vote = county
        # 6d: Print the county results to the terminal.
        curr_county_print = f"{county}: {county_vote_percent :.1f}% ({current_votes:,})\n"
        print(curr_county_print)
        txt_file.write(curr_county_print)
    # 7: Print the county with the largest turnout to the terminal.
    #print(f"Largest county is {Largest_county_Vote} and the vote is {Largest_County_turnout:,}")
    Largest_county_Turnout_print = (
            f"\nLargest county Turnout\n"
            f"-------------------------\n"
            f"{Largest_county_Vote }: {Largest_County_turnout:,}\n\n"
            f"-------------------------\n")
    print(Largest_county_Turnout_print)
        # 8: Save the county with the largest turnout to a text file. 
    txt_file.write(Largest_county_Turnout_print)
    # print(county_vote) 
    # print(candidate_votes)      
    # print(candidate_options)
    # print(County_Votes)
    # print(County_list)
    # print(total_votes)        
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #  If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # votes to the terminal.
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #     # Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage} " " % of the vote.")
        # Determine if the votes are greater than the winning count.
       # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")