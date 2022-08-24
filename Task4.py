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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
callers = []
numbers_to_avoid = []

for i in calls:
    callers.append(i[0])
    numbers_to_avoid.append(i[1])

for j in texts:
    numbers_to_avoid.append(j[0])
    numbers_to_avoid.append(j[1])

telemarkerter  = set(callers) - set(numbers_to_avoid)
telemarkerter  = sorted(set(telemarkerter))

print("These numbers could be telemarketers: ")
for i in telemarkerter:
    print(i)


    
