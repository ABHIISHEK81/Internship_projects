from src.intake import intake_check, generate_clarifying_questions
from src.planner import generate_plan
from src.verifier import verify_response

def run_pipeline(llm, retriever, user_input):
    missing = intake_check(user_input)

    if missing:
        return {
            "clarifying_questions": generate_clarifying_questions(missing)
        }

    query = user_input["query"]
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([d.page_content for d in docs])

    response = generate_plan(llm, context, query)
    verification = verify_response(response)

    return {
        "response": response,
        "verification": verification
    }
