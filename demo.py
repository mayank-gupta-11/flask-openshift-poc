from flask import Flask, request
app = Flask(__name__)

def get_method():
    return "get method call was successfull!"

def post_method():
    return "post method call was successfull!"

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        content = request.json
        query_param = request.args
        print(content)
        print("-----------------------")
        print("-----------------------")
        print(query_param.get("name"))
        return get_method()
    if request.method == 'POST':
        content = request.json
        query_param = request.args
        print(content)
        print("-----------------------")
        print(content["delimeter"])
        print("-----------------------")
        print(query_param.get("name"))
        return post_method()
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
