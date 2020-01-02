from flask import Flask

app = Flask(__name__)

@app.route('/')
def.index():
    return 'Hellllloo'


#update 2019-01-02 21-51