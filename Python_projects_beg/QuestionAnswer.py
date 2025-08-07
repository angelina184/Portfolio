# vscode uses wrong python interpreter for this project
from termcolor import colored
import random 

QUESTION = 'question'
ANSWER = 'answer'
OPTIONS = 'options'

#questions  {question['question']}
#answer    question[ANSWER]
#options    question[OPTIONS]

def show_questions(index,question,answer,options):
    print(f"Question {index}: {question}")       
    for letter,answer in options.items():
        print(f"{letter}. {answer}")
    user_answer = input("Your answer: ").upper().strip()  
    return user_answer


def run(questions):
    right_answers = 0
    # can use module random for getting questions in random order
    random.shuffle(questions)
    #(0, questions[0])(1, questions[1]) ...
    for index , question in enumerate(questions,1):
            get_answer = show_questions(index,question['question'],question[ANSWER], question[OPTIONS])       
            correct_answer = question[ANSWER]
            
            for letter,answer in question[OPTIONS].items():
                print(f"{letter}. {answer}")
            if get_answer == correct_answer:
                print(colored("Correct!","green"))
                print("")
                right_answers += 1
            else:
                print(colored(f"Wrong! The correct answer is {correct_answer}","red"))
                print("")
    print(f"Quiz over! Your final score is {right_answers} out of {index}")        

def main():
    questions = [
        {
            QUESTION:"What is the capital of France?", 
            ANSWER:"C",
            OPTIONS: {
                "A": "Berlin",
                "B": "Madrid",
                "C": "Paris",
                "D": "Rome"
            }
        },
        {
            QUESTION:"Which planet is known as the red planet?", 
            ANSWER:"B",
            OPTIONS: {
                "A": "Earth",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Saturn"
            }
        },
        {
            QUESTION:"What is the largest ocean on Earth?", 
            ANSWER:"D",
            OPTIONS: {
                "A": "Atlantic",
                "B": "Indian",
                "C": "Arctic",
                "D": "Pacific"
            }
        }
    ]
    run(questions)

if __name__ == '__main__':
    main()