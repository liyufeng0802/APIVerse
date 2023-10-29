from gpt_module import GPT_module
from action_module.questioner import Questioner
import re
"""
arg_retriever: 
"""
class Arg_Retriever:
    def __init__(self):
        self.llm_model = GPT_module()
    
    def fill_curl(self, conversation, curl):
        # Format question
        prompt = f"After I ask user \"{conversation[-2]}\" for getting value in this crul {curl}. Then user answer me \"{conversation[-1]}\". fill in the crul. Only give the curl, not any other sense in your response."
        # Ask llm what is missing and ask for value
        response = self.llm_model.query(prompt)
        save_reponse = response[:]
        print(response)
       
        # return the question
        curl = None
        result= re.findall(r'["\']((curl).*?)["\']', response)
        try:
            curl = result[0]
        except:
            curl = save_reponse
        return curl

    
