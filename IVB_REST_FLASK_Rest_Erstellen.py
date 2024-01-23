from flask import Flask, request
from flask_restful import Api, Resource
from dataclasses import dataclass
from flask.json import jsonify

app = Flask(__name__)
api = Api(app)

@dataclass
class Question:
    id: int
    text: str
    answer: str

questions = [
    Question(id=1, text="What is the capital of France?", answer="Paris"),
    Question(id=2, text="Who wrote Romeo and Juliet?", answer="William Shakespeare"),
    # ... add more questions as needed
]

class QuestionResource(Resource):
    def get(self, question_id):
        # Holen einer Frage über die ID
        question = next((q for q in questions if q.id == question_id), None)
        return jsonify(question)

    def put(self, question_id):
        # Ändern einer Frage
        question = next((q for q in questions if q.id == question_id), None)
        data = request.get_json()
        question.text = data["text"]
        question.answer = data["answer"]
        return jsonify(question)

    def delete(self, question_id):
        # Löschen einer Frage
        global questions
        questions = [q for q in questions if q.id != question_id]
        return {"message": "Question deleted successfully"}

api.add_resource(QuestionResource, '/question/<int:question_id>')

class RandomQuestionResource(Resource):
    def get(self):
        # Holen einer zufälligen Frage
        import random
        random_question = random.choice(questions)
        return jsonify(random_question)

api.add_resource(RandomQuestionResource, '/question/random')

class AllQuestionsResource(Resource):
    def get(self):
        # Holen aller Fragen
        return jsonify(questions)

api.add_resource(AllQuestionsResource, '/questions')

if __name__ == '__main__':
    app.run(debug=True)
