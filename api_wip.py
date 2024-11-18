qs = {
    "q1": {"question": "Are Circles Square?", "answers": ["Yes", "No"]},
    "q2": {"question": "Are Apples Blue?", "answers": ["Yes", "No"]},
    "q3": {"question": "Does the Willow Lean?", "answers": ["Yes", "No"]},
    "q4": {"question": "Ten More Buttons?", "answers": ["Yes", "No"]},
    "q5": {"question": "Lovely Potatoes?", "answers": ["Yes", "No"]},
    "q6": {"question": "Vested Kittens In Red?", "answers": ["Yes", "No"]}
}

qs["q1"]["question"] = "Bend it Over"
qs["q1"]

import requests

def fetch_trivia_question():
    # API endpoint for Trivia API
    url = "https://the-trivia-api.com/v2/questions"

    try:
        # Make a GET request to fetch a trivia question
        response = requests.get(url)

        # Raise an HTTPError if the request was unsuccessful
        response.raise_for_status()

        # Parse the response JSON
        questions = response.json()
        
        # Assuming the response contains a list of questions
        if questions:
            question_data = questions[0]  # Get the first question
            question = question_data.get("question", "No question found")
            correct_answer = question_data.get("correctAnswer", "No answer found")
            incorrect_answers = question_data.get("incorrectAnswers", [])
            
            print("Question:", question)
            print("Correct Answer:", correct_answer)
            print("Incorrect Answers:", incorrect_answers)
        else:
            print("No questions available.")

    except requests.exceptions.RequestException as e:
        print("Error fetching trivia question:", e)

# Fetch a trivia question
fetch_trivia_question()
