import csv, os

# Funtion that returns a vector from a specific dataset, returns
# the column number from a data set
def data_to_vector(data_set_csv, number_column_return):
    vector = []
    for row in data_set_csv:
        vector.append(list(row)[2])
    return vector

# Funtion that will create a list with a unique spot for each candidate
def counting_votes(votes_per_candidate):
    candidates = [votes_per_candidate[0]]
    for i in range(1,len(votes_per_candidate)):
        new_candidate = False
        for j in range(len(candidates)):
            if votes_per_candidate[i] == candidates[j]:
                new_candidate = False
                break
            else:
                new_candidate = True
        if new_candidate == True:
            candidates.append(votes_per_candidate[i])
    return candidates

#creating the path and reading the csv.file
path_file = os.path.join("Resources","election_data.csv")
with open(path_file, 'r') as csvfile:
    csv_votes_per_candidate = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csv_votes_per_candidate)
    vector_candidates = data_to_vector(csv_votes_per_candidate, 3)

# Calling at the functions and saving the results to be shown
voted_candidates = counting_votes(vector_candidates)
total_votes = len(vector_candidates)
votes_for_each = []
for i in range(len(voted_candidates)):
    votes_for_each.append(vector_candidates.count(voted_candidates[i]))
percentages = []
for i in range(len(voted_candidates)):
    percentages.append(round(votes_for_each[i]/total_votes*100,3))
index_winner = votes_for_each.index(max(votes_for_each))

# Printing the results in Bash
print('Election Results \n-------------------------------------')
print(f"Total Votes: {total_votes} \n-------------------------------------")
for i in range(len(voted_candidates)):
    print(f"{voted_candidates[i]}: {percentages[i]}% ({votes_for_each[i]})")
print("-------------------------------------")    
print(f"Winnner: {voted_candidates[index_winner]}")
print("-------------------------------------")    

# Zipping the columns together and printing into a csv file.
zipped = zip(vector_candidates, percentages, votes_for_each)
output_path = os.path.join('Resources','Results_PyPoll.csv')
with open(output_path, 'w', newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter= ',')
    writer.writerow(["Election Results"])
    writer.writerow(["Total Votes:",total_votes])
    writer.writerows(zipped)
    writer.writerow(["Winner:",voted_candidates[index_winner] ])