from gpt_module import GPT_module
import requests
import re
import json


class Import_module:
    
    def __init__(self):
        self.data = []
    

    def addNewURL(self, url):
        html_format = requests.get(url)
        text = html_format.text
        prompt = "On this website, is there an API documentation?\n" + text + "\nIf there is no API documentation on the webpage, print me a No. If there is API documentation, can you write me the curl requests with those APIs that do not require authentication including descriptions?  I want you summarize them in an python array list format, where each list element is a tuple, ex [(curl request1, description for the endpoint1), (curl request2, description for the endpoint2)]"
        # print(prompt)
        test_model = GPT_module()
        response = test_model.query(prompt)
        curl_requests = ""
        found = False
        for c in response:
            if c == "[":
                found = True
                continue
            if c == "]" and found:
                break
            if found:
                curl_requests += c
        regex = r"\(.*\)"
        curl_list = re.findall(regex, curl_requests)
        self.saveCurlList(curl_list)
    
    def saveCurlList(self, curl_list):
        self.data = []
        for c in curl_list:
            curl, description = c.split(",")
            dic = {}
            dic["curl"] = curl[1:]
            dic["description"] = description[:-1]
            self.data.append(dic)

        file_path = "database/data_2.json"
        with open(file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def get_summary(self):
        f = open('database/data_2.json')
        data = json.load(f)
        description_list = []
        for curl in data:
            description_list.append({"description" : curl["description"]})
        prompt = f"Given a list of descriptions of each API, a human can help the user call the corresponding API. Write me a summary descript in first person of what the user can ask me to do. \nPlease list all the questions users can ask me.\n(Avoid using technical words, such as \"Fetch\", \"Retrieve\", \"Load\" and so on)\n{description_list}"
        model = GPT_module()
        response = model.query(prompt)
        return response
    
    def get_jsonResponse(self):
        return self.data
        
