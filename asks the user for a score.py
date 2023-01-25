#   1. Write a program that asks the user for a score.
#   2. If the score is greater than or equal to 90, print "Grade A".
#   3. If the score is greater than or equal to 80, print "Grade B".
#   4. Otherwise, print "Grade C".
#   5. If the score is greater than or equal to 94, print "Excellent!".
#   6. Otherwise, print "Good Job!".
score = int(input("What is your score? "))

if score >= 90:
    print("Grade A")
    if score >= 94:
        print("Excellent!")
    else:
        print("Good Job!")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")
