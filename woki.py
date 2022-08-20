from rawi import Question
 
question_prompt = [
    "What colour is snow?\n(a) green\n(b) white\n(c) purple\n\n",
    "Can fish walk?\n(a) Yes\n(b) No\n\n",
    "What colour is strawberry?\n(a) Red\n(b) Yellow\n(c) Green\n\n"
]

questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.") 

run_test(questions)        