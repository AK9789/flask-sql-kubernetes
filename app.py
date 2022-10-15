from flask import Flask,request, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your secret key'


@app.route('/')
def hello():
    return jsonify("Hello")

@app.route('/init')
def init():
    mydb = mysql.connector.connect( host="mysql", user="root", password="password") #change the host to hostname that you gave in database container as conatiner_name
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE cr")
    return jsonify("DB Created")

@app.route('/table')
def table():
    mydb = mysql.connector.connect( host="mysql", user="root", password="password", database="cr")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE temp(name VARCHAR(255), rarity VARCHAR(255), elixir INT(30))")
    return jsonify("Table Created")

@app.route('/list')
def list():
    mydb = mysql.connector.connect( host="mysql", user="root", password="password", database="cr")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM temp")
    output = mycursor.fetchall()
    return jsonify(output)

@app.route('/post',methods=['POST'])
def post():
    mydb = mysql.connector.connect( host="mysql", user="root", password="password", database="cr")
    mycursor = mydb.cursor()
    new_name = request.form["name"]
    new_rarity = request.form["rarity"]
    new_elixir = request.form["elixir"]
    sql = "INSERT INTO temp (name, rarity, elixir) VALUES (%s, %s, %s)"
    mycursor.execute(sql, (new_name, new_rarity, new_elixir))
    mydb.commit()
    return jsonify("Record Added")

if __name__ == "__main__":
    app.run(debug=1)