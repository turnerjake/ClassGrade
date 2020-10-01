""" PSEUDOCODE
create list

capture input
append
capture input
append
capture input
append
capture input
append
capture input
append

print message to user """

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades / 3

print("Average grade: {0:.2f}%".format(result))
