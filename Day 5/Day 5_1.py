# Exercise 1 - Average Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_num = 0
average_height = 0
for i in range(0, len(student_heights)):
    average_height += student_heights[i]
    total_num += 1
average_height /= total_num
print(round(average_height))
