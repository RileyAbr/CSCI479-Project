import pandas
import time
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

#start timer
start = time.time()

# Import the Data
dataset = pandas.read_csv("C:/Users/Matthew Martin/Documents/School/Data Mining/Project/store_data.csv")

records = []
#puts data from csv into python list
for i in range(0, 500):
    #prints i just to be able to see where it breaks in a csv, if it breaks
    print(i)
    records.append([str(dataset.values[i,j]) for j in range(0, 20)])
    
#removes the 'nan' from the documents
for i,j in enumerate(records):
    while 'nan' in records[i]: 
        records[i].remove('nan')

te = TransactionEncoder()
oht_ary = te.fit(records).transform(records, sparse=True)
sparse_df = pandas.SparseDataFrame(oht_ary, columns=te.columns_, default_fill_value=False)
results = apriori(sparse_df, min_support=0.001, use_colnames=True)
results['length'] = results['itemsets'].apply(lambda x: len(x))
results = results[ (results['length'] >= 2) & (results['support'] >= 0.01) ]
print(results)

with open('output.txt', 'w') as f:
    for _list in results._values:
        for _string in _list:
            f.write(str(_string) + ' ')
        f.write('\n')

#ends time and prints how long it took
end = time.time()
print("Total time to run:")
print(end - start)


