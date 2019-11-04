#!flask/bin/python
from flask import Flask

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__' :
    app.run(debug= True)