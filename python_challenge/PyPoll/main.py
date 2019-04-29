import os
import csv  

candidates = {}    #init a dictionary called candidates, 
                    #candidates will have a key: candidate name , value: votes

#csv file will be in Resources dir at our script level
csvfile = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvfile, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    tot_votes = 0           # running variable used for each vote count

    for row in csvreader:
        #print(row)
        tot_votes = tot_votes + 1       #running TOTAL of ALL votes (REQUESTED)
        if row[2] in candidates:        # check if candidate is already in our dict
            candidates[row[2]] += 1     #they are, so add 1 to the votecount
        else:
            candidates[row[2]] = 1      #theyre not there yet so make it 1

print("Election Results\n")     
print("-----------------------\n") 
print("Total Votes: " + str(tot_votes) + "\n")
print("-----------------------\n") 
for key, value in candidates.items():
    print(key + ": " + str(round((value/tot_votes * 100),2)) + "% (" + str(value) + ")")    # REQUESTED
print("-----------------------\n") 
print("Winner: " + max(candidates, key=candidates.get) + "\n")          #  REQUESTED
print("-----------------------") 

foutname = "election_data_analysis.txt"
print("Printing this financial analysis to: " + str(os.getcwd()) + "/" + foutname)
with open(foutname, 'w') as file_object:
    file_object.write("Election Results\n")
with open(foutname, 'a') as file_object:
    file_object.write("-----------------------\n")
    file_object.write("Total Votes: " + str(tot_votes) + "\n")
    file_object.write("-----------------------\n")
    # find the %s now, by looping thru the dictionary
    for key, value in candidates.items():
        file_object.write(key + ": " + str(round((value/tot_votes * 100),2)) + "% (" + str(value) + ")\n")
    file_object.write("-----------------------\n") 
    file_object.write("Winner: " + max(candidates, key=candidates.get) + "\n")
    file_object.write("-----------------------") 
    
print("\nFinished!")
