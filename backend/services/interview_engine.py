import random

class InterviewBot:
    def __init__(self, job_description):
        self.job_description = job_description
        self.questions = [
            "Can you describe your most challenging project?",
            "Which technologies are you most comfortable with?",
            "How does your experience align with this role?",
            "Tell me about a time you solved a difficult problem.",
            "What do you think are your key strengths?"
        ]
        self.current_index = 0

    def get_next_question(self):
        if self.current_index < len(self.questions):
            q = self.questions[self.current_index]
            self.current_index += 1
            return q
        return "That’s all for now! You can type 'end session' to finish."

    def get_follow_up(self, answer):
        if len(answer.split()) < 5:
            return "Could you elaborate a bit more on that?"
        elif "team" in answer.lower():
            return "What role did you play in the team?"
        else:
            return self.get_next_question()
