from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # => When a request is make for "/", execute the function and return the result of the function to the user
def index():
    #return "Welcome to Flask!"

    print(request.method)
    data = {"name":"Magesh"}
    return jsonify(data)

app.run(port=8080, debug=True)