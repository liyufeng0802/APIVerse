from action_module.rag_gpt import RAG_GPT

"""
API router: Base on user intented action (API call, eg. "Tell me some cat fact")
            then route to correct CRUL to work for this action
"""
class Router:
    # variable
    def __init__(self):
        pass
    
    def detector(self, user_intent):
        """
        Input:
        - user_intent: some action they want to do (eg. "Tell me some cat fact")

        Output:
        - curl: the corresponding curl for this intent
        - description: the description of this specific API
        """
        # Ask llm what is this intent want to call which API
        prompt = f"""Base on this user intent {user_intent}, what crul I should call? Only give me a single curl command with good format, be consistent with quotation usage, e.g.  "curl -H 'Accept: application/json' https://icanhazdadjoke.com/" e.g. avoid other special characters."""
        llm_model = RAG_GPT()
        response = llm_model.query(prompt)
        # return the RAW format CURL, and its description
        return response
