'''from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = int("5000"))'''
    

    '''

    the server will reply in the following manner:

    GET /hello
    Hello John Doe

    GET /hello?name=Luis
    Hello Luis

    '''

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
