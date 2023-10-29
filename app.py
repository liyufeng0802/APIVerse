from flask import Flask, request, jsonify
from import_module.import_module import Import_module
from action_module.caller import Caller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# import url from the list
@app.route('/import', methods=['GET'])
def importNewDocument():
    print("importing new document")
    args = request.args
    url = args.get("url")
    print(f"importing url: {url}")
    importer = Import_module()
    importer.addNewURL(url)
    jsonResponse = importer.get_jsonResponse()
    data = {
            "listData" : jsonResponse,
            "summary" : importer.get_summary(),
        }
    # data = {
    #     "listData" : [
    #         {
    #             "title" : "title1",
    #             "url" : "url1",
    #             "summary" : "summary1",
    #         },
    #         {
    #             "title" : "title2",
    #             "url" : "url2",
    #             "summary" : "summary2",
    #         },
    #         {
    #             "title" : "title3",
    #             "url" : "url3",
    #             "summary" : "summary3",
    #         },
    #     ],
    #     "summary" : "summary 1231231231231",
    # }
    return jsonify(data) 

# chat windom input
@app.route('/query', methods=['POST'])
def readQuery():
    # input conversation []
    print("start processing query")
    j = request.json
    # print(j)
    clist = j["conversation"]
    print(f"conversation list: {clist}")
    user_input = clist[-1]
    print(f"user input: {user_input}")
    caller = Caller()
    summary = caller.process_user_request(user_input, clist)
    print(f"summary: {summary}")
    clist.append(summary)
    # Conversation List
    # API response summary
    data = { 
            "conversation" : clist, 
            "summary" : summary, 
        }
    return jsonify(data)    

if __name__ == '__main__':
    importer = Import_module()
    importer.erase_current_curl()
    app.run(host='0.0.0.0', port=105)