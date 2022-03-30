from flask import Flask, render_template, request

#create app    
app = Flask(__name__)

#Ensure templates are auto-reloaded
#app.config["TEMPLATES_AUTO_RELOAD"] = True

#create db
import sqlite3 as sql
con = sql.connect('users.db', check_same_thread=False)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=["GET","POST"])
def form():   
    if request.method == "POST":    
        first_name = request.form["first_name"]
        surname = request.form["surname"]
        gender = request.form["gender"]
        pseudo = request.form["pseudo"]
    #create table  
        with con:
            con.execute('''
                    CREATE TABLE IF NOT EXISTS users 
                    (first_name TEXT NOT NULL, 
                     surname TEXT NOT NULL, 
                     gender TEXT NOT NULL, 
                     pseudo TEXT NOT NULL UNIQUE)
                    ''')
            con.execute("INSERT INTO users VALUES ('{}','{}','{}','{}')".format( first_name, surname, gender, pseudo))
            con.commit()
            #con.close()
    return render_template("welcome.html", first_name=first_name, surname=surname, gender=gender, pseudo=pseudo)

#create users page to check
@app.route("/users")
def users():
    rows = con.execute("SELECT * FROM users")
    return render_template("users.html", rows=rows)
    
if __name__ == '__main__':
    app.run(debug=True)