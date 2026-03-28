def verify_response(response):
    return {
        "has_citations": "Citations:" in response,
        "has_answer": "Answer / Plan:" in response,
        "has_reasoning": "Why:" in response
    }
