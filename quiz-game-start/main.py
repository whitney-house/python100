from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

quiz_b = QuizBrain(question_bank)

# if still has questions, continue to check
while quiz_b.still_has_questions():
    quiz_b.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz_b.score}. ")
