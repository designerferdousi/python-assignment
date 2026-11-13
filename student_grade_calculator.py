# 1. Ask For Student's Name
name = input("Enter student name:")

# 2. Ask For Marks of 3 Subjects
math = float(input("Enterr Math marks:"))
english = float(input("Enter English marks:"))
python = float(input("Enter Python marks:"))

# 3. Calculator Total and Average Marks
total = math + english + python
average = total/3

# 4. Determine grade
if average >= 80:
  grade = "A+" 
elif average >= 70:
  grade = "A"
elif average >= 60:
  grade ="B"
elif average >= 50:
  grade = "C"
else:
  grade = "F"

# 5. Display final result
print(f"Student Name: {name}")
print(f"Total Marks: {total:.0f}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
