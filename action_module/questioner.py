from gpt_module import GPT_module
"""
Questioner: Check if the curl are ready, ask user specific field to fill in
"""
class Questioner:
    # variable
    AFTER_PROMT = """
                Based on this API request and API description,  what value is missing in the request? Please get me a sentence to ask the user for these required values. Only tell me the question sentence.
                Example: Please tell me what is the book's name.
                """

        
    
    def __init__(self):
        self.llm_model = GPT_module()
    
    def question(self, curl, description):
        """
        Input:
        - user_intent: some action they want to do (eg. "Tell me some cat fact")

        Output:
        - curl: the corresponding curl for this intent
        - description: the description of this specific API
        """
        # Format question
        prompt = f"CURL: {curl}\nDescription:{description}\n" + self.AFTER_PROMT
        # Ask llm what is missing and ask for value
        response = self.llm_model.query(prompt)
        # return the question
        return response

    
