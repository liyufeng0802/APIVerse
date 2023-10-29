from gpt_module import GPT_module
import json
import requests
"""
Caller: call the "Ready-to-call" CRUL, and parse the API response to human-tone response
"""
class Caller:
    # variables

    def __init__(self):
        pass
    
    def call(self, curl, description):
        """
        Input:
        - curl: the ready-to-call curl
        - description: description of this API, use for response convertion (in purpose of LLM understanding)

        Output:
        - response: human-tone response for this API
        """
        # API call with curl => API response
        # use API response => make the human-tone response with LLM

        # return human-tone summary of the API response
        response = None

        return response


    # Validate the input curl
    def curl_ready(self, input_curl):
        try:
            response = requests.head(input_curl)
            return response.status_code < 400  # Valid if status code is less than 400 (2xx or 3xx)
        except requests.RequestException:
            return False  # Invalid if there was a request exception (4xx or 5xx)

    # Given info, returns human-understandable response
    def curl_call(self,input_info, desc):
        test_model = GPT_module()

        # Prompt to chatGPT
        input_info = json.dumps(input_info)
        information_from_AI = test_model.query('{desc}\nHere is the API description, and I have the following response after making a request, If there are no errors, extract useful information and generate human-understandable information and write a short paragraph only about the response content, no API status, no API response description, and only include the information but nothing else. If there are errors, give humans understandable information about the error.\n' + input_info)
        return information_from_AI