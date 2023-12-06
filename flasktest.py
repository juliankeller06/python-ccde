from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
import millionenshow
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
app.static_folder = 'test'
Session(app)

class Question:
    def __init__(self, question_text, level, options, correct_index):
        self.question_text = question_text
        self.level = level
        self.options = options
        self.correct_index = correct_index



def get_random_question(level, questions):
    eligible_questions = [q for q in questions if q.level == level]
    return random.choice(eligible_questions) if eligible_questions else None



@app.route('/')
def index():
    session.clear()
    session['level'] = 1
    return redirect(url_for('question'))

@app.route('/question')
def question():
    if session['level'] > 5:
        feedback = 'Glückwunsch! Du hast alle Fragen richtig beantwortet und das Spiel gewonnen!'
        return render_template('flask_session.html', feedback=feedback)

    questions = millionenshow.read_questions("millionaire.txt")
    question = get_random_question(session['level'], questions)
    session['question'] = question

    return render_template('flask_session.html', question=question, level=session['level'])

@app.route('/answer/<int:answer_index>')
def answer(answer_index):
    question = session['question']

    if not question or 'correct_index' not in question.__dict__:
        return redirect(url_for('question'))  # Redirect to get a new question if there's an issue

    user_answer = answer_index
    if millionenshow.check_answer(question, user_answer):
        feedback = 'Fine'
        session['level'] += 1
    else:
        feedback = 'Wrong answer. Game over!'


    return render_template('flask_session.html', feedback=feedback, question=question, level=session['level'])



if __name__ == '__main__':
    app.run(debug=True)
