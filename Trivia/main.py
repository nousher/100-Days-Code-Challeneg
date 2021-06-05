import question_model 
import quiz_brain
from data import  Gk_Question
from data import Geography_Question 
import logging, sys
import report_Card as rp


logging.basicConfig(stream=sys.stderr, level=logging.INFO)
print("Welcome to Trivia!!!!")
Username=input("Please enter your full name: \n")
NeedReport=input("Do you want a Report Card? \n")
QuestionSet=input("Please enter A for General Knowledge Questions or enter B for Geography Questions? \n")

def run():
    tempQuestion = QuestionSet.lower()
    if  tempQuestion == "a":
        question_data = Gk_Question
    elif tempQuestion == "b":
        question_data = Geography_Question
    else:
        print("Please choose option A or B.")
        quit()

    data=[]
    for question in question_data:
            
        ques = question["question"]
        answer = question["correct_answer"]
        logging.debug('self.question = %s', ques)
        logging.debug('self.answer = %s', answer)
        dataSet=question_model.SetQuestionsAnswers(ques,answer)
        data.append(dataSet)

    quizReq=quiz_brain.ProcessHandler(data)

    while quizReq.checkLastQuestion():
       score=quizReq.presentQuestion(logging)

    if NeedReport == "Yes" or NeedReport == "yes":
        if score/10 > 0.7:
            rp.CreateReportCard(Username, score)
        else:
            print("Sorry you have failed the Trivia!")

if __name__ == "__main__":
    run()