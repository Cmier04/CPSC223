import csv

# Step 1: Create the initial CSV file with student data
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

# Write the data to a CSV file
csv_file_path = 'students.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Step 2: Read the CSV file and process the data
students = []

with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# Task 1: Calculate the total number of students
total_students = len(students)

# Task 2: Calculate the average age per class
class_ages = {}
class_counts = {}

for student in students:
    student_class = student['Class']
    student_age = int(student['Age'])
    
    if student_class not in class_ages:
        class_ages[student_class] = 0
        class_counts[student_class] = 0
        
    class_ages[student_class] += student_age
    class_counts[student_class] += 1

class_averages = {cls: class_ages[cls] / class_counts[cls] for cls in class_ages}

# Task 3: Create a new CSV file for 10th grade students
filtered_data = [["Name", "Roll No."]]
for student in students:
    if student['Class'] == '10th':
        filtered_data.append([student['Name'], student['Roll No.']])

# Write the filtered data to a new CSV file
filtered_csv_file_path = '10th_grade_students.csv'
with open(filtered_csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_data)

# Print the results
print(f"Total number of students: {total_students}")
print("Average age per class:")
for cls, avg_age in class_averages.items():
    print(f"{cls}: {avg_age:.2f} years")
