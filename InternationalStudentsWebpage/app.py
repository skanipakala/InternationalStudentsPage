# import necessary libraries
from flask import Flask, render_template, url_for, jsonify

# create Flask app
app = Flask(__name__)

# create data for students
students = [
    {
        "name": "John Doe",
        "country": "USA",
        "quote": "I love studying abroad!"
    },
    {
        "name": "Jane Smith",
        "country": "Canada",
        "quote": "I am learning so much from this experience!"
    }
]

# define routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students")
def student_list():
    return jsonify(students)

@app.route("/student/<int:id>")
def student_detail(id):
    student = students[id-1]
    return render_template("student_detail.html", student=student)

# run the app
if __name__ == "__main__":
    app.run(debug=True)
