from flask import Flask, request, jsonify
from services.resume_parser import extract_text_from_file
from services.match_engine import calculate_match_score, generate_suggestions
from services.interview_engine import InterviewBot

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


interview_sessions = {}

@app.route('/')
def home():
    return "Resume Match and Mock Interview API is running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    try:
        resume = request.files['resume']
        job_description = request.form['job_description']

        resume_text = extract_text_from_file(resume)
        match_score = calculate_match_score(resume_text, job_description)
        suggestions = generate_suggestions(resume_text, job_description)

        response = {
            "match_score": round(match_score, 2),
            "suggestions": suggestions
        }

        if match_score >= 80:
            response["message"] = "Great match! Would you like to start a mock interview?"

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/start_interview', methods=['POST'])
def start_interview():
    user_id = request.form.get('user_id', 'guest')
    job_description = request.form['job_description']

    bot = InterviewBot(job_description)
    first_question = bot.get_next_question()

    interview_sessions[user_id] = bot
    return jsonify({"question": first_question})


@app.route('/chat', methods=['POST'])
def chat():
    user_id = request.form['user_id']
    user_answer = request.form['answer']

    if user_answer.lower() == "end session":
        interview_sessions.pop(user_id, None)
        return jsonify({"message": "Interview session ended. Great job!"})

    bot = interview_sessions.get(user_id)
    if not bot:
        return jsonify({"error": "No active session found. Start a new interview."}), 400

    follow_up = bot.get_follow_up(user_answer)
    return jsonify({"question": follow_up})


if __name__ == '__main__':
    app.run(debug=True)
