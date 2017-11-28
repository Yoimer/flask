''' the server will reply in the following manner:

    GET /hello
    Hello John Doe

    GET /hello?name=Luis
    Hello Luis '''

from flask import Flask, url_for

app = Flask(__name__)

from flask import request

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = int("5000"))
