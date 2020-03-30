import os  
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#saves the info from csv into two lists
def vector_data(data_file):
    dates = []
    values = []
    for item in data_file:
        dates.append(list(item)[0])
        values.append(float(list(item)[1]))
    return [dates, values]

# From vector this function must return the
#  adn the mean [max, indexMax, min, indexMin, mean]
def max_min_indexes(vector):
    max = vector[0]
    min = vector[0]
    indexMax = 0
    indexMin = 0
    suma = 0
    for i in range(len(vector)):
        if vector[i] > max:
            indexMax = i
            max = vector[i]
        if vector[i] < min:
            indexMin = i
            min = vector[i]
        suma = suma + vector[i]
    return [max, indexMax, min, indexMin, round(suma/len(vector), 2)]



with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    listed_values = vector_data(csvreader)
    max_min_values = max_min_indexes(listed_values[1])

# Assigning the values for printing 
list1 = [
        "Total Months: ", "Total: ", "Average Change: ",
        "Greatest Increase in Profits: ","Greatest Decrease in Profits: "
        ]
list2 = [
        str(len(listed_values[0])), str(sum(listed_values[1])),
        str(max_min_values[4]),
        f"{listed_values[0][max_min_values[1]]} (${max_min_values[0]})",
        f"{listed_values[0][max_min_values[3]]} (${max_min_values[2]})"
        ]
print("Finacial Analysis")
print("__________________________________")
for i in range(len(list1)):
    print(list1[i] + list2[i])

zipped = zip(list1,list2)  
output_path = os.path.join('Resources','Results_PyBank.csv')
with open(output_path, 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Financial Analysis', ' '])
    writer.writerows(zipped)
