from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Hi we just hit our flask server")
    return """<html>
        Hello, world!
        <a href="/html"> Click here for html </a>
        <br>
        <a href="/stylish"> Click here for css </a>
    </html>"""

@app.route("/html")
def show_interesting_html():
    return """<html>
        <body> 
            <h1>This is a big header</h1>
            <h2>This is a sub header</h2>
            <h3>This is a sub sub header</h3>
            <h4>This is a sub sub sub header</h4>
        </body>
    </html>"""

@app.route("/stylish")
def show_interesting_css():
    return """<html>
        <head>
            <style>
                h1 {
                    color:red;
                }
            </style>
        </head>
        <body> 
            <h1>This is a big header</h1>
            <h2>This is a sub header</h2>
            <h3>This is a sub sub header</h3>
            <h4>This is a sub sub sub header</h4>
        </body>
    </html>"""

@app.route("/postie", methods=["POST"])
def post():
    return "I'm a post response"

if __name__ == "__main__":
    app.run()
