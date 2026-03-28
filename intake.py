def intake_check(user_input):
    required_fields = ["completed_courses", "target_program", "term"]
    return [f for f in required_fields if f not in user_input]

def generate_clarifying_questions(missing_fields):
    mapping = {
        "completed_courses": "Which courses have you completed?",
        "target_program": "What is your target program?",
        "term": "Which term are you planning for?"
    }
    return [mapping[m] for m in missing_fields]
