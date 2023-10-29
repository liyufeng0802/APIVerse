from flask import Flask, request, jsonify
from import_module.import_module import Import_module
from action_module.caller import Caller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# import url from the list
@app.route('/import', methods=['GET'])
def importNewDocument():
    # args = request.args
    # url = args.get("url")
    # importer = Import_module()
    # importer.addNewURL(url)
    # jsonResponse = importer.get_jsonResponse()
    # data = {
    #         "listData" : jsonResponse,
    #         "summary" : importer.get_summary(),
    #     }
    data = {
        "listData" : [
            {
                "title" : "title1",
                "url" : "url1",
                "summary" : "summary1",
            },
            {
                "title" : "title2",
                "url" : "url2",
                "summary" : "summary2",
            },
            {
                "title" : "title3",
                "url" : "url3",
                "summary" : "summary3",
            },
        ],
        "summary" : "summary 1231231231231",
    }
    return jsonify(data) 

# chat windom input
@app.route('/query', methods=['POST'])
def readQuery():
    # input conversation []
    j = request.json
    # print(j)
    clist = j["conversation"]
    # print(clist)
    user_input = clist[-1]
    caller = Caller()
    summary = caller.process_user_request(user_input)
    # Conversation List
    # API response summary
    data = { 
            "conversation" : clist, 
            "summary" : summary, 
        }
    return jsonify(data)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)