#!/usr/bin/python3
# ver 3.5
#
# Example to RESTful web services
# ref: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return 'Hello World!'

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

#
# GET method
#
# We have a get_tasks function that is associated with the /todo/api/v1.0/tasks URI,
# and only for the GET HTTP method.
#
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    #return jsonify({'tasks': tasks})
    return jsonify({'tasks' : [make_public_task(task) for task in tasks]})   # add ['url']

#
# Second version of GET method
#
# Here we get the id of the task in the URL, and Flask translates it into the task_id
# argument that we receive in the function
#
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    #return jsonify({'task': task[0]})
    return jsonify({'task': make_public_task(task[0])})  # add ['url']

#
# If JSON data is expected by client, this allow 404 response in JSON
#
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#
# POST method
# Use to insert a new item in the task database
#
# Example to post json
# ref: https://stackoverflow.com/questions/9733638/post-json-using-python-requests
#
# >>> import requests
# >>> r = requests.post('http://tomyworld.pythonanywhere.com/todo/api/v1.0/tasks', json={'title':'Read a book'})
# >>> r.status_code
# >>> r.json()
#
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

#
# PUT method
#
# For the update_task function, trying to prevent bugs by doing exhaustive checking of the input arguments.
# Need to make sure that anything that the client provided us is in the expected format before we incorporate
# it into our database
#
# Example (for Windows):
# $curl -i -H "Content-Type: application/json" -X PUT -d "{\"done\":true}" http://tomyworld.pythonanywhere.com/todo/api/v1.0/tasks/2
#
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

#
# DLETE method
#
# Example (for Windows):
# $ curl -i -X DELETE http://tomyworld.pythonanywhere.com/todo/api/v1.0/tasks/3
#
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

#
# Improving the web service interface
#
# Returning task ids we can return the full URI that controls the task, so that clients get the URIs
# ready to be used. For this we can write a small helper function that generates a "public" version
# of a task to send to the client:
#
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

#
# Securing a RESTful web service
#
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

    #
    # To prevent browsers from showing authentication dialogs and let our client application
    # handle the login
    #
    #return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run()
