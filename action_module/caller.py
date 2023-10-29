from gpt_module import GPT_module
from action_module.router import Router
import json
import requests
import subprocess
import re


"""
Caller: call the "Ready-to-call" CRUL, and parse the API response to human-tone response
"""
class Caller:
    # variables

    def __init__(self):
        pass

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
    
    # Given user propmt, decide what functions to call
    def process_user_request(self, user_request):
        router = Router()

        complete_resopnse = router.detector(user_request)
        # print(complete_resopnse)
        
        # You should call the following curl: "curl -H 'Accept: application/json' https://icanhazdadjoke.com/".
        result= re.search(r'["\']((curl).*?)["\']', complete_resopnse)
        curl = result.group(1)
        # print(curl)

        decs = self.find_description(curl)
        # print("Desc: ", decs)
        
        process = subprocess.Popen(curl, stdout=subprocess.PIPE, shell=True)

        # Read the output of the command
        output, _ = process.communicate()

        # Print the output
        print(output.decode('utf-8'))

        return self.curl_call(output.decode('utf-8'), decs)

    def find_description(self, curl):
        f = open('database/data_2.json')
        data = json.load(f)
        for entry in data:
            entry_curl = entry["curl"]
            description = entry["description"]
            if entry_curl in curl or curl in entry_curl:
                return description
        return "" 