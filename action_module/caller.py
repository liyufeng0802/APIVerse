from gpt_module import GPT_module
from action_module.router import Router
import json
import requests
import subprocess 
from action_module.questioner import Questioner
from action_module.arg_retriever import Arg_Retriever
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
    def process_user_request(self, user_request, conversation):
        # Only when currrent_curl doesn't exist, we need rounter to find corresponding curl
        f = open('database/current_curl.json')
        current_url_data = json.load(f)
        if "curl" not in current_url_data or current_url_data["curl"] == None:
            router = Router()

            complete_resopnse = router.detector(user_request)
            print("complete_resopnse: ", complete_resopnse, "\nTHE END OF")
            
            curl = None
            # You should call the following curl: "curl -H 'Accept: application/json' https://icanhazdadjoke.com/".
            result= re.search(r'(^["\'](curl).*)', complete_resopnse)
            try:
                curl = result.group(1).strip('"').strip("'")
            except:
                curl = complete_resopnse
            print(curl)
            decs = self.find_description(curl)
            # print("Desc: ", decs)

            # put the curl and decs back to json file
            current_url_data["curl"] = curl
            current_url_data["description"] = decs

            with open('database/current_curl.json', "w") as json_file:
                json.dump(current_url_data, json_file, indent=4)
        else:
            # user input parameter
            arg_retriever = Arg_Retriever()
            curl_after_fill = arg_retriever.fill_curl(conversation, current_url_data["curl"])
            current_url_data["curl"] = curl_after_fill
            with open('database/current_curl.json', "w") as json_file:
                json.dump(current_url_data, json_file, indent=4)


        # get curl from current url
        curl, decs = self.get_current_curl()

        print("curl: ", curl)

        if self.check_missing_params(curl):
            # ask questioner
            questioner = Questioner()
            ask_question = questioner.question(curl, decs)
            return ask_question
        else:
            # can directly call
            process = subprocess.Popen(curl, stdout=subprocess.PIPE, shell=True)

            # Read the output of the command
            output, _ = process.communicate()

            # Print the output
            print(output.decode('utf-8'))

            if output.decode('utf-8') == '':
                response = requests.get(curl.split(" ")[-1])
                return response.url

            return self.curl_call(output.decode('utf-8'), decs)
    
    def get_current_curl(self):
        f = open('database/current_curl.json')
        current_url_data = json.load(f)
        return current_url_data["curl"], current_url_data["description"]

    def find_description(self, curl):
        f = open('database/live.json')
        data = json.load(f)
        for entry in data:
            entry_curl = entry["curl"]
            description = entry["description"]
            if entry_curl in curl or curl in entry_curl:
                return description
        return "" 
    
    def check_missing_params(self, curl):
        for c in curl:
            if c == "{" or c == "}":
                return True
        return False