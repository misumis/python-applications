from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, my Students!!'
  
if __name__ == '__main__':
    app.run(debug=True)