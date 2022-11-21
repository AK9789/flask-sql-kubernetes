from flask import Flask,request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("Hello")

@app.route('/init')
def init():
    mydb = mysql.connector.connect( host="localhost", user="root", password="root") #change the host to hostname that you gave in database container as conatiner_name
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE cr")
    return jsonify("DB Created")

@app.route('/table')
def table():
    mydb = mysql.connector.connect( host="localhost", user="root", password="root", database="cr")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE temp(id INT(20), name VARCHAR(255), specialization VARCHAR(255), mobile VARCHAR(255), email VARCHAR(255), address VARCHAR(255))")
    return jsonify("Table Created")

@app.route('/list')
def list():
    mydb = mysql.connector.connect( host="localhost", user="root", password="root", database="cr")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM temp")
    output = mycursor.fetchall()
    return jsonify(output)

@app.route('/post',methods=['POST'])
def post():
    mydb = mysql.connector.connect( host="localhost", user="root", password="root", database="cr")
    mycursor = mydb.cursor()
    new_id = request.form["id"]
    new_name = request.form["name"]
    new_specialization = request.form["specialization"]
    new_mobile = request.form["mobile"]
    new_email = request.form["email"]
    new_address = request.form["address"]
    sql = "INSERT INTO temp (id, name, specialization, mobile, email, address) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, (new_id, new_name,new_specialization, new_mobile, new_email, new_address))
    mydb.commit()
    return jsonify("Record Added")

@app.route("/doclist/<int:id>", methods=["GET", "PUT"])
def specific_doctor(id):
    mydb = mysql.connector.connect( host="localhost", user="root", password="root", database="cr")
    mycursor = mydb.cursor()
    doctor = None
    if request.method == "GET":
        mycursor.execute("SELECT * FROM temp WHERE id=%s", (id,))
        rows = mycursor.fetchall()
        for r in rows:
            doctor = r
        if doctor is not None:
            return jsonify(doctor)
        else:
            return "Something wrong"

if __name__ == "__main__":
    app.run()
