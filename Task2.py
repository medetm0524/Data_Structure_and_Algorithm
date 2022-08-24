"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
calls_out = []
calls_in = []

for i in range(len(calls)):
    calls_out.append(calls[i][0])
    calls_in.append(calls[i][1])
    
all_calls = calls_out + calls_in
unique_call = list(set(all_calls))

call_duration = []
for i in unique_call:
    duration = 0
    for j in range(len(calls)):
        if i == calls[j][0] or i==calls[j][1]:
            duration+=int(calls[j][3])
        else:
            pass
    call_duration.append(duration)

max_duration_index = call_duration.index(max(call_duration))
print(" {} spent the longest time, {} seconds, on the phone during September 2016.".format(
    unique_call[max_duration_index],call_duration[max_duration_index]))