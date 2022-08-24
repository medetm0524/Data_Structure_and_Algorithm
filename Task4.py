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
phone_market = []
phone_user = []

for i in calls:
    if i[0][0:3]=='140':
        phone_market.append(i[0])
    
    if i[1][0:3]=='140':
        phone_user.append(i[1])

for j in texts:
    if j[0][0:3]=='140':
        phone_user.append(j[0])
    if j[1][0:3]=='140':
        phone_user.append(j[1])

phone_market = set(phone_market) - set(phone_user)
phone_market = list(map(int, phone_market))
phone_market = sorted(set(phone_market))

print("These numbers could be telemarketers: ")
for i in phone_market:
    print(i)


    
