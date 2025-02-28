from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello !'

@app.route('/test')
def test():
    return request.args.get('name')

if __name__ == '__main__':
    app.run(port=5000)