import random
import logging, sys


class ProcessHandler():

    def __init__(self, dataSet):
        self.questionNumber=0
        self.score=0
        self.q_list=dataSet
    
    def checkLastQuestion(self):
        isLastQuestion=self.questionNumber < len(self.q_list)
        return isLastQuestion
    
    def presentQuestion(self, logging):
        current_question=self.q_list[self.questionNumber]
        self.questionNumber += 1
        logging.debug('self.question = %s', current_question.question)
        logging.debug('self.answer = %s', current_question.answer)
        userAns=input(f"Q{self.questionNumber}. {current_question.question} ? \n")
        score=self.checkAnswer(userAns,current_question)
        return score

    def checkAnswer(self, ans, currentQuestion):

        if ans == "stop" or ans == "quit" or ans == "q":
            logging.info("Thank you for playing!!!!")
            quit()
        if ans == "t" or ans == "T":
            ans = "true"

        if ans.lower() == currentQuestion.answer.lower():
            self.score +=1
        else:
            print("wrong answer")
        print("\n")
        logging.info("Current Score is %s \n", self.score)
        score=self.score
        return score
        