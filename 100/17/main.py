from data import question_data
import requests
from question_model import Question
from quiz_brain import QuizBrain
q_bank = []
for q in question_data:
    q_bank.append(Question(q["text"],q["answer"]))

brain = QuizBrain(q_bank)

while brain.still_has_questions():
    brain.next_question()
