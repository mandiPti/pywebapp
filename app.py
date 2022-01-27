from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    html = "<h3>Hello World from Flask App!</h3><h1>HUI-DI-HUI-BUI!</h1>" 
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
