# Exercise 1 - Average Height 

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
average = 0
count =0
for H in student_heights:
    average += H
    count += 1

average_height = round(average/count)
print(average_height)