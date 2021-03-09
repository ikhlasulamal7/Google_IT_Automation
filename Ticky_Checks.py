#!/usr/bin/env python3
import sys
import re
import operator
import csv
#Just Testing
# Dict: Count number of entries for each user
per_user = {}  # Splitting between INFO and ERROR
# Dict: Number of different error messages
error_counter = {}

# * Read file and create dictionaries
with open('syslog.log') as file:
    # read each line
    for line in file.readlines():
        # regex search
        # * Sample Line of log file
        # "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        # Populates error dict with ERROR messages from log file
        # Populates per_user dict with users and default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        # Populates per_user dict with users logs entry
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]["INFO"] += 1
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['ERROR'] += 1


# Sorted by USERNAME
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()

# * Create CSV file user_statistics
with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in per_user_list:
                csvw.writerow({'Username': key, 'INFO': value['INFO'], 'ERROR': value['ERROR']})

# * Create CSV error_message
error_counter = {}
error_user = {}

#This function will read each line of the syslog.log file and check if it is an error or an info message.
def search_file():
    with open('syslog.log', "r") as myfile:
     for line in myfile:
        if " ERROR " in line:
            find_error(line)
            add_user_list(line)
    return


#If it is an error it will read the error from the line and increment into the dictionary
def find_error(str):
    match = re.search(r"(ERROR [\w \[]*) ", str)
    if match is not None:
        aux = match.group(0).replace("ERROR ", "").strip()
        if aux == "Ticket":
         aux = "Ticket doesn't exist"
        if not aux in error_counter:
            error_counter[aux] = 1
        else:
            error_counter[aux] += 1
    return

#This whill read the user from the string and add to the error or the info counter depending on the op number
def add_user_list(str):
    match = re.search(r'\(.*?\)', str)
    user = match.group(0)
    userA = user.strip("()")
    if not userA in error_user:
        error_user[userA] = 1
    else:
        error_user[userA] += 1
    return

#This function will read the list, arrange it and return a tuple with the dictionary items
def sort_list(list):
    s = sorted(list.items(), key=operator.itemgetter(1), reverse=True)
    return s

#This is an extra function which will read the value of a user in the error dictionary and return its value if key exists

#This function writes both csv files
def write_csv():
    with open('error_message.csv', 'w', newline='') as output:
        fieldnames = ['Error', 'Count']
        csvw = csv.DictWriter(output, fieldnames=fieldnames)
        csvw.writeheader()
        for key, value in error_counter:
            csvw.writerow({'Error': key, 'Count': value})
    return

#This function adds zero to the other dictionary in case that user is not a key, it will add a key with the user and value 0

search_file()
error_counter = sort_list(error_counter)
write_csv()
