from flask import Flask, render_template, request, session, redirect, json
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
