import os,csv

# Define the input file path
infile="PyPoll\Resources\election_data.csv"

#Initialize Variables
counter = 0
candidates = []
candidates_dict = {}

#Open the csv file
with open(infile) as election_data:
    reader = csv.reader(election_data)
   
   #Read the header row
    header = next(reader)
   
# Loop through each row in the csv
    for row in reader:
    
       counter = counter + 1 

       #check if the candidate name is already in the list, if not add it otherwise count it
       if row[2] not in candidates:
        candidates.append(row[2])
        candidates_dict[row[2]] = 1
      
       else:
        candidates_dict[row[2]] += 1
      

# Print the results
output=(
f"Election Results\n"
f"{'-' * 20 }\n"
f"Total Votes:    {counter}\n"
f"{'-' * 20}\n"
)

for candidate, votes in candidates_dict.items():
    output += f"{candidate}: {votes / counter * 100:.3f}% ({votes})\n"
    output += f"{'-' * 20}\n"     

    #printing the winner 
winner_name = max(candidates_dict, key=candidates_dict.get)
output += f"Winner: {winner_name}\n"
output += f"{'-' * 20}\n"


print(output)

with open("PyPoll/analysis/election_results.txt" , "w") as text_file:
    text_file.write(output)


