class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num  = 0
        self.correct = 0
        self.incorrect = 0

    def next_question(self):
            current_q = self.question_list[self.question_num]
            self.question_num += 1
            answer = input("Q.{}: {} (True/False)?: ".format(self.question_num, current_q.text))
            self.check_answer(answer,current_q.answer)

    def still_has_questions(self):
       return self.question_num < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.correct += 1
        else:
            self.incorrect += 1
        print("Correct/Incorrect ({}/{})".format(self.correct,self.incorrect))


# ask user q
# check if answer is right
# check if we're at end of quiz
# attrib: question_number = 0; question_list
# method: next_question()
