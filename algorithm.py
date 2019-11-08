from apyori import apriori
import pandas
import time

#start timer
start = time.time()

# Import the Data
dataset = pandas.read_csv("C:/Users/Matthew Martin/Documents/School/Data Mining/Project/store_data.csv")

records = []
#puts data from csv into python list
for i in range(0, 7500):
    #prints i just to be able to see where it breaks in a csv, if it breaks
    print(i)
    records.append([str(dataset.values[i,j]) for j in range(0, 20)])

#removes the 'nan' from the documents
for i,j in enumerate(records):
    while 'nan' in records[i]: 
        records[i].remove('nan')

#applying the apriori itemset mining to the records list
results = list(apriori(records, min_support=0.01, min_confidence=.2, min_lift=1, min_length=3))
print("Number of results:")
print(len(results))
print("\n")

#prints first entry in list (for testing)
print("First Entry:")
print(results[0])
print("\n")

#writes to a file each of the different rules so that we don't have to run this everytime to see the results

with open('output.txt', 'w') as f:
    for _list in results:
        for _string in _list:
            f.write(str(_string) + ' ')
        f.write('\n')

#ends time and prints how long it took
end = time.time()
print("Total time to run:")
print(end - start)

