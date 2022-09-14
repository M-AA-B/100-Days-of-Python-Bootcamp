# Exercise 2 - High Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for i in range(0, len(student_scores)):
    if student_scores[i] > highest_score:
        highest_score = student_scores[i]
print(f"The highest score in the class is: {highest_score}")
