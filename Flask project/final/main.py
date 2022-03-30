#imports
from flask import Flask, render_template, request
import mysql.connector as mariadb

#create app
app = Flask(__name__)

#db connection
conn = mariadb.connect(host='localhost', user='root', password='root')
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS usersdb")
cur.execute("USE usersdb")

# homepage link
@app.route("/")
def home():
  return render_template("home.html")

#welcome page route
@app.route('/welcome')
def testForm():
  return render_template("welcome.html")

# adding users
@app.route('/', methods=['GET', 'POST'])
def register():
  if (request.method == 'POST'):
    firstname = request.form['firstname']
    surname = request.form['surname']
    gender = request.form['gender']
    title = "Mr" if gender == "M" else "Ms" # M or F specified in Html
    pseudo = request.form['pseudo']
    cur.execute("CREATE DATABASE IF NOT EXISTS usersdb")
    cur.execute("USE usersdb")
    cur.execute("CREATE TABLE  IF NOT EXISTS Users(firstname VARCHAR(30) NOT NULL, surname VARCHAR(30) NOT NULL, gender VARCHAR(15) NOT NULL, pseudo VARCHAR(20) NOT NULL UNIQUE )")
    cur.execute("INSERT INTO Users VALUES ('{}','{}','{}','{}')".format( firstname, surname, gender, pseudo))
    conn.commit()
    #conn.close()
    #cur.close()
    
    return render_template("welcome.html", firstname=firstname, surname=surname, gender=gender, pseudo=pseudo)
  else:
    return render_template("users.html")

# users page
@app.route('/users', methods=['GET'])
def users():
  if request.method == 'GET' :
    cur.execute("SELECT * FROM Users")
    lignes = cur.fetchall()
    return render_template('users.html',rows=lignes) 
  else:
    return render_template("users.html")

#launching
if __name__ == "__main__":
  app.run(debug=True)
