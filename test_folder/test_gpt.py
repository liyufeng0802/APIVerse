from gpt_module import GPT_module
from RAG import TriggerDetector
from import_module.import_module import Import_module
import requests
import re
import json

def main():
    """url = "https://icanhazdadjoke.com/api#endpoints"
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
    print(curl_requests)
    regex = r"\(.*\)"
    curl_list = re.findall(regex, curl_requests)
    # print(curl_list)

    data = []
    for c in curl_list:
        curl, description = c.split(",")
        dic = {}
        dic["curl"] = curl[1:]
        dic["description"] = description[:-1]
        data.append(dic)
    print("the dict is:", data)

    file_path = "database/live.json"
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)"""
    importer = Import_module()
    print(importer.get_summary())

if __name__ == "__main__":
    main()