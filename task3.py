questions = [
    "What's 4 times 3? ",
    "What's 60 - 6? ",
    "What's 9 times 9, plus 2? "

]
answers = [12, 54, 83]

index = 0

# Loop through the math questions
while index < len(questions):
    reply = input(questions[index])

    if int(reply) == answers[index]:
        print("Correct!")
        index = index + 1
    else:
        print("Incorrect! Please try again.")

print("Well done! Thanks for playing.")