from crewai.tools import tool

@tool("Classify User Request")
def classify_user_request(query):
    """Classify the user's request into a specific intent category and recommend the appropriate agent to handle it."""
    query = query.lower()
    if "dashboard" in query:
        return {
            "intent": "dashboard",
            "recommended_agent": "Data Analyst Agent"
        }
    elif "machine learning" in query:
        return {
            "intent": "data_science",
            "recommended_agent": "Data Scientist Agent"
        }
    return {
        "intent": "mixed",
        "recommended_agent": "Both"
    }

@tool("Create Agent Work Plan")
def create_agent_work_plan(intent):
    """Create a work plan for the agent based on the classified intent."""
    plans = {
        "dashboard": [
            "Profile dataset",
            "Generate KPIs",
            "Create dashboard"
        ],
        "mixed": [
            "Profile data",
            "Quality checks",
            "ML opportunities"
        ]
    }
    return {
        "steps": plans.get(intent, plans["mixed"])
    }

@tool("Summarize Chat History")
def summarize_chat_history(history):
    """Summarize the chat history into a concise summary."""
    return " ".join(history)

@tool("Estimate Context Usage")
def estimate_context_usage(text):
    """Estimate the number of tokens used in the context window."""
    words = len(text.split())
    return {
        "estimated_input_tokens": words,
        "context_window": 8192
    }

@tool("Validate Final Response Structure")
def validate_final_response_structure(response):
    """Validate that the final response contains all required sections."""
    required = [
        "Direct Answer",
        "Dataset Summary",
        "Recommended KPIs"
    ]
    missing = []
    for r in required:
        if r not in response:
            missing.append(r)
    return {
        "valid": len(missing) == 0,
        "missing": missing
    }