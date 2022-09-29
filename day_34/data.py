import requests
import html

params = {
    "amount": 10,
    "type": "boolean"
}

result = requests.get(url="https://opentdb.com/api.php", params=params)

result.raise_for_status()
result = result.json()['results']

question_data = [
    {"question": html.unescape(question['question']),
     "correct_answer": question['correct_answer']}
    for
    question in result]
