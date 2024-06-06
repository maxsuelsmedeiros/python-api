from flask import Flask

app=Flask(__name__)

@app.route('/')
def home() -> str:
    return 'Hello Beautiful World!'

app.run(port=5000)