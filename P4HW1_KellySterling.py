# Sterling Kelly
# November 27, 2025
# P4HW1
# Program collects scores using a loop, checks for valid input,
# drops the lowest score, finds the average, and displays the grade.

num_scores = int(input("How many scores do you want to enter? "))

scores = []
count = 0

while count < num_scores:
    score = float(input("Enter score #" + str(count + 1) + ": "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(count + 1) + " again: "))

    scores.append(score)
    count = count + 1

lowest = min(scores)

modified_scores = scores.copy()
modified_scores.remove(lowest)

average = sum(modified_scores) / len(modified_scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("--------Results")
print("Lowest Score :")
print(lowest)
print("Modified List:", modified_scores)
print("Scores Average:")
print(format(average, ".2f"))
print("Grade :", grade)
