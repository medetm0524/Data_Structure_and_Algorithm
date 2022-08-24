"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
area_codes_B = []
mobile_pref_B = []
telemarketers_B = []

for i in calls:
    if i[0][1:4]== '080':
        if i[1][0]=='(':
            res = re.findall(r'\(.*?\)', i[1])
            area_codes_B.append(res[0][1:-1])
        if i[1][0]=='7' or i[1][0]=='8' or i[1][0]=='9':
            mobile_pref_B.append(i[1][0:4])


area_code_B = list(map(int, area_codes_B))
area_code_B = sorted(set(area_code_B))

print("The numbers called by people in Bangalore have codes:")
for i in area_code_B:
    print('0'+str(i))
   
    
mobile_pref_B = set(mobile_pref_B)
mobile_pref_B = list(map(int, mobile_pref_B))
mobile_pref_B = sorted(set(mobile_pref_B))

for i in mobile_pref_B:
    print(i)


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
call_from_B = 0
call_to_B = 0
for each_record in calls:
    if "080" in each_record[0]:
        call_from_B+=1
        if "080" in each_record[1]:
            call_to_B+=1
            
percentage = call_to_B/call_from_B
print("{:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage*100))

            
        

