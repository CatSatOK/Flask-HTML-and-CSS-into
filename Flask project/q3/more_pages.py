from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message_home = "This is the home page")

@app.route("/next")
def next():
    return render_template("next.html")

if __name__ == "__main__":
    app.run()
