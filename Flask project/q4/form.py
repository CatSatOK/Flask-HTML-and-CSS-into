from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=["GET","POST"])
def text_box():
    first_name = request.form["first_name"]
    surname = request.form["surname"]
    gender = request.form["gender"]
    pseudo = request.form["pseudo"]
    #add .upper() ?
    return render_template("welcome.html", first_name=first_name, surname=surname, gender=gender, pseudo=pseudo)
    
if __name__ == '__main__':
    app.run(debug=True)