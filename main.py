from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

# open trivia database online
# TODO change difficulty
difficulty = ["easy", "medium", "hard"] # diffulty[0, 1 or 2]
trivia_url = "https://opentdb.com/api.php"
parameters= {
  "amount": 10,
  "difficulty": difficulty[0], 
  "type": "boolean"
  
}
response = requests.get(trivia_url, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#while quiz.still_has_questions(): # mainloop in QuizInterface is also a loop. so dont use two loops
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
