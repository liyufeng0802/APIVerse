from flask import Flask, request, jsonify
from gpt_module import GPT_module
import requests
import json
from action_module.router import Router 

from import_module import import_module
from action_module.rag_gpt import RAG_GPT

from action_module.caller import Caller
import subprocess
import re
def main():
    # # url = "https://api.spaceflightnewsapi.net/v3/articles/21284"
    # url = "https://api.spaceflightnewsapi.net/v4/articles/"
    # # url = "https://api.spaceflightnewsapi.net/v4/articles/21284"
    # # url = "https://picsum.photos/200"


    # # Making a GET request
    # response = requests.get(url)

    # # print("The response is:")
    # # print(response)
    # # print(response.url)

    # json_data = response.json()
    # # print(".josn is: ")
    # # print(json_data)
    # # data = json.dumps(json_data)
    # data = json_data
    # print(curl_call(data))

    print(process_user_request("Get me a random joke"))

def process_user_request(user_request):
    router = Router()

    complete_resopnse = router.detector(user_request)
    print(complete_resopnse)
    
    # You should call the following curl: "curl -H 'Accept: application/json' https://icanhazdadjoke.com/".
    result= re.search(r'"((curl).*?)"', complete_resopnse)
    curl = result.group(1)
    print(curl)

    decs = find_description(curl)
    print("Desc: ", decs)
    
    process = subprocess.Popen(curl, stdout=subprocess.PIPE, shell=True)

    # Read the output of the command
    output, _ = process.communicate()

    # Print the output
    print(output.decode('utf-8'))

    caller = Caller()

    return caller.curl_call(output.decode('utf-8'), decs)

def find_description(curl):
    f = open('database/data_2.json')
    data = json.load(f)
    for entry in data:
        entry_curl = entry["curl"]
        description = entry["description"]
        if entry_curl in curl or curl in entry_curl:
            return description
    return ""


# Given info, returns human-understandable response
# def curl_call(input_info):
    # test_model = GPT_module()

    # We make the request
    # Extract the URL using regex
    # httpPath = input_curl_command[6:-1]
    
    # Make the GET request
    # terminal_response = requests.get(httpPath).text

    # Prompt to chatGPT
    # input_info = json.dumps(input_info)
    # information_from_AI = test_model.query('I have the following response after making a request,  If there are no errors, extract useful information and generate human-understandable information and write an article, and only include the information but nothing else, If there are errors, give humans understandable information about the error.\n' + input_info)
    # return information_from_AI

if __name__ == "__main__":
    main()