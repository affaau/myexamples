'''Server demo
Work with client (send_post_request.py)

To run this server:
$ set FlASK_APP = flask_app
$ flask run
'''
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "heLLo, wORLd!"

    if request.method == "POST":
        propertyId = request.json['propertyId']
        secretKey = request.json['secretKey']
        msg = "Property ID is {}\nSecretKey is {}\n".format(propertyId,secretKey)
        return msg
    
if __name__ == "__main__":
    app.run()