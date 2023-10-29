from gpt_module import GPT_module
import requests
import re
import json
from bs4 import BeautifulSoup


class Import_module:
    
    def __init__(self):
        self.erase_current_curl()
        self.data = []
    

    def addNewURL(self, url):
        if self.cache_hit(url):
            return
        html_format = requests.get(url)
        text = html_format.text
        text = clean_html(text)
        prompt = f"On this website (at the bottom of this prompt), is there an API documentation?\nIf there is no API documentation on the webpage, print me a No. If there is API documentation, can you write me the curl requests with those APIs that do not require authentication including descriptions?  I want you summarize the available APIs in an python array list format, where each list element is a tuple, ex [(curl request1, description for the endpoint1), (curl request2, description for the endpoint2)]. If using any of the quotes for the tuples, only use single quote. also, avoid any other special chars, such as $, #, etc, just give me clean tuple lists. When include the text content, don't include the comma of thar text, since it gonna be conflit with the comma of my list items. you have to use single quoteBelow is the content of the website: {text}"
        # print(prompt)
        test_model = GPT_module()
        response = test_model.query(prompt)
        # print("Response: ", response)
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
        # print(curl_requests)
        regex = r"\(.*\)"
        curl_list = re.findall(regex, curl_requests)
        # print("the list: ", curl_list)
        self.saveCurlList(curl_list)
        self.caching(url)
    
    def saveCurlList(self, curl_list):
        self.data = []
        for c in curl_list:
            curl, description = c.split(",")
            dic = {}
            dic["curl"] = curl[1:]
            dic["description"] = description[:-1]
            self.data.append(dic)

        file_path = "database/live.json"
        with open(file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def get_summary(self):
        f = open('database/live.json')
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

    def caching(self, url):
        cache_path = "database/cache.json"

        # Read existing data from the JSON file
        with open(cache_path, 'r') as file:
            existing_data = json.load(file)

        # Modify the data (append a new item to a list, for example)
        new_item = {"url": url, "json": self.data}
        existing_data["items"].append(new_item)

        with open(cache_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
    
    def cache_hit(self, url):
        hit = False
        cache_path = "database/cache.json"

        # Read existing data from the JSON file
        with open(cache_path, 'r') as file:
            existing_data = json.load(file)

        for item in existing_data["items"]:
            if item["url"] == url:
                hit = True

                self.data = item["json"]
                file_path = "database/live.json"
                with open(file_path, "w") as json_file:
                    json.dump(self.data, json_file, indent=4)

                break

        return hit
    
    def clean_cache(self):
        cache_path = "database/cache.json"

        # Modify the data (append a new item to a list, for example)
        new_item = {"items": []}

        with open(cache_path, 'w') as file:
            json.dump(new_item, file, indent=4)

    def erase_current_curl(self):
        curr_path = "database/current_curl.json"
        clean_curl = {"curl": None, "description": None}
        with open(curr_path, "w") as json_file:
            json.dump(clean_curl, json_file, indent=4)


def clean_html(html_text):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_text, "html.parser")

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()  # Remove the tag and its content

    # Get the text content of the HTML
    text = soup.get_text(separator='\n', strip=True)

    # Return the cleaned text
    return text
