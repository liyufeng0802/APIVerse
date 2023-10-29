from flask import Flask, request, jsonify
from gpt_module import GPT_module
import requests
import json
from action_module.router  import Router 

from import_module.import_module import Import_module
from action_module.rag_gpt import RAG_GPT

from action_module.caller import Caller
import subprocess
import re

app = Flask(__name__)

# import url from the list
@app.route('/import', methods=['GET'])
def importNewDocument():
    args = request.args
    url = args.get("url")
    importer = Import_module()
    importer.addNewURL(url)
    jsonResponse = importer.get_jsonResponse()
    data = { 
            "listData" : jsonResponse, 
            "summary" : importer.get_summary(), 
        }
    return jsonify(data) 
    # API response:
    # Humman tone summary
    # Json => list of curl

# chat windom input
@app.route('/query', methods=['POST'])
def readQuery():
    # input conversation []
    j = request.json
    print(j)
    clist = j["conversation"]
    print(clist)
    user_input = clist[-1]
    summary = process_user_request(user_input)
    # Conversation List
    # API response summary
    data = { 
            "conversation" : clist, 
            "summary" : summary, 
        }
    return jsonify(data) 

# Given user propmt, decide what functions to call
def process_user_request(user_request):
    router = Router()

    complete_resopnse = router.detector(user_request)
    print(complete_resopnse)
    
    # You should call the following curl: "curl -H 'Accept: application/json' https://icanhazdadjoke.com/".
    result= re.search(r'["\']((curl).*?)["\']', complete_resopnse)
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







    
    



    



    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)