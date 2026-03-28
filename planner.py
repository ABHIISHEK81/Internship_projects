SYSTEM_PROMPT = """
You are a catalog-grounded academic assistant.

Rules:
- Only use retrieved context
- If unsure say you do not have the information
- Always include citations

Output format:

Answer / Plan:
Why:
Citations:
Clarifying questions:
Assumptions / Not in catalog:
"""

def generate_plan(llm, context, query):
    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{query}
"""
    return llm.invoke(prompt)
