"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file
infile = open("employee_data.csv", "r")
data = csv.reader(infile, delimiter=",")
next(infile)

# create an empty dictionary
dict = {""}


# use a loop to iterate through the csv file
for row in data:
    employee_fname = row[1]
    employee_lname = row[2]
    employee_department = row[3]
    employee_title = row[4]
    employee_salary = row[5]

    # check if the employee fits the search criteria
    if employee_title == "CSR":
        if employee_department == "Marketing":
            print(
                "Manager Name: ",
                employee_fname,
                employee_lname,
                " Current Salary: ",
                employee_salary,
            )

print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
for row in data:
    employee_fname = row[1]
    employee_lname = row[2]
    employee_department = row[3]
    employee_title = row[4]
    employee_salary = row[5]

    if employee_title == "CSR":
        if employee_department == "Marketing":
            new_salary = (int(row[5]) * 0.10) + int(row[5])
            dict.append(employee_fname + employee_lname, new_salary)
            print(dict)
