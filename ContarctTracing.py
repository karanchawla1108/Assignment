# Assignment Brief
# Contact tracing is an important method of keeping infections under control. Whenever somebody is identified to be infected with COVID-19, health workers try to quickly identify anybody who has been in contact with them. These people may also have been infected and could infect other people, so getting them tested and isolated early is essential.

# Suppose there is a public health system designed for government staff to quickly identify people who may have come into contact with an infected individual. As part of this scheme, all shops and public venues are required to log who visits that location each day, and submit these logs to the central database. If an individual is found to have been infectious for some period, this log can be consulted to find who was at the same location as this individual on the same day, and so may have been infected. These people can then be contacted so that they can be tested.

# Description of the task
# Write a version of this contact tracing program. It should:

# Prompt for the name of the infected patient
# Prompt for the date on which to search for contacts
# Find all individuals who were at the same location as the infected patient on the given date
# Print a formatted list of individuals who need to be contacted
# Technical details of approach
# This assignment will require you to demonstrate your ability to:

# Load data from a CSV file
# Print formatted strings
# Define and use functions
# Use looping and conditional branching
# Research and use standard Python libraries (e.g., datetime)
# Follow PEP-8 style recommendations
# Your approach should make good use of functions. In particular, the logic to identify matches of individuals who should be contacted should be contained in a function that you call from the main body of your code. You can also add additional functions as you see fit. All functions should include appropriate docstrings.

# Extra Details
# Your code should generate one report line for each person detected
# If somebody is detected for more than one trip, you should use the first reported address visited by the tested patient
# Your code should work for any date, not just those in the supplied CSV
# Example of functionality
# Your code should prompt for details of a single patient (patient name and testing date) and then list all matching contacts. An example of the correct operation of this program is as follows. Note that your code will be tested on other data, so you should not rely upon the contents of the CSV file provided. The same file structure will be used in all cases.

# The person who was tested positive: Arthur
# When was the test? 09/02/2021
# Doreen should stay at home for next 10 days due to the trip to 4 Arizona Street on 02, Sep 2021
# John should stay at home for next 10 days due to the trip to 4 Arizona Street on 02, Sep 2021
# William should stay at home for next 10 days due to the trip to 04 Kim Circle on 02, Sep 2021
# ​







import csv
import datetime as dt


def read_data(file_read):
    data = []#list to store data

    with open(file_read, newline='') as file:
         for line in csv.DictReader(file):
             data.append(line)
    return data

#Use the function to open file.
file_read = 'contacts.csv'
data = read_data(file_read)


# Person name to search for.
name = str(input("The person who was tested positive: "))
date = input("When was the test? ")
date1 = dt.datetime.strptime(date, '%m/%d/%Y')

infected_person_address = []# Using set to rid of duplicacy.

for entry in data:
   entry_date = dt.datetime.strptime(entry['Date'], '%m/%d/%Y')
   if entry['User'] == name and entry_date == date1:
      infected_person_address.append(entry['Address'])
      
#Now find who visited on this address.
contacts = {}#Dictionary to store name with address.
for entry in data:
    entry_date = dt.datetime.strptime(entry['Date'], '%m/%d/%Y')                               
    if entry['Address'] in infected_person_address and entry_date == date1:
       contacts[entry['User']] = entry['Address']
                                      
if name in contacts:
   contacts.pop(name)       

for user, address in contacts.items():
    
    print(f"{user} should stay at home for next 10 days due to the trip to {address} on {date1.strftime('%d, %b %Y')}")
 





     
     
      
      