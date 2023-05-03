from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="vaccination"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def search():
    reg_no = request.form["reg_no"]
    cursor = db.cursor()
    query = "SELECT * FROM students WHERE RegNo = %s"
    cursor.execute(query, (reg_no,))
    student = cursor.fetchone()
    if student:
        name = student[1]
        status = student[2]
        return render_template("result.html", name=name, status=status)
    else:
        message = f"No student with registration number {reg_no} found."
        return render_template("error.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
