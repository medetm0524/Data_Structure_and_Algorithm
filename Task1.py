"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
calls_out = []
calls_in = []
texts_out = []
texts_in = []

for i in range(len(calls)):
    calls_out.append(calls[i][0])
    calls_in.append(calls[i][1])

for j in range(len(texts)):
    texts_out.append(texts[j][0])
    texts_in.append(texts[j][1])
    
total_list = calls_out+calls_in+texts_out+texts_in
unique_list = set(total_list)

print("There are {} different telephone numbers in the records.".format(len(unique_list)))
