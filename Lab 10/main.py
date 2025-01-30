#Christine Mier
#December 9, 2024
#This file creates a csv file with student information and calculates and prints both the total number of students and the average age per class

import csv
from collections import defaultdict
import os

data = [
    ["Name", "Age", "Gender", "Class", "Section", "Roll No."],
    ["John", 16, "Male", "10th", "A", 1],
    ["Sara", 15, "Female", "9th", "B", 2],
    ["David", 17, "Male", "11th", "C", 3],
    ["Emily", 15, "Female", "10th", "D", 4],
    ["Michael", 16, "Male", "10th", "A", 5],
    ["Lisa", 14, "Female", "9th", "B", 6],
    ["Chris", 18, "Male", "12th", "C", 7],
    ["Ava", 15, "Female", "10th", "D", 8],
    ["Robert", 16, "Male", "10th", "A", 9],
    ["Emma", 14, "Female", "9th", "B", 10]
]

'''Declare filename and open file in write mode'''
filename = 'students.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

'''create a student data list and store student grades. read file'''
students_data = []
grades = defaultdict(list)

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students_data.append(row)
        grades[row['Class']].append(int(row['Age']))

'''get the total number of students and print'''
total_students = len(students_data)
print(f'Total number of students: {total_students}')

'''calculate average ages in each grade'''
average_ages = {}
for grades, ages in grades.items():
    average_ages[grades] = round(sum(ages) / len(ages))

print('Average age per class: ')
for grade, average_age in average_ages.items():
    print(f'{grades}: {int(average_age):}')
    
'''create a new csv file that contains only names and roll numbers of students in 10th grade'''
filename_10th = 'students_10th.csv'
with open(filename_10th, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Roll No.'])
    for student in students_data:
        if student['Class'] == '10th':
            writer.writerow([student['Name'], student['Roll No.']])

'''Confirm new file has been created'''
if os.path.exists('students_10th.csv'):
    print(f'New CSV file created: {filename_10th}')
